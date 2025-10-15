import sys
import json
import pandas as pd

def process_ticket_data(json_file_path, ticket_id):
    """
    JSONファイルから指定されたチケットIDのスケジュール情報を抽出し、CSVファイルに変換する関数。

    Args:
        json_file_path (str): 入力するJSONファイルのパス。
        ticket_id (str): 抽出対象のチケットID。
    """
    try:
        # JSONファイルを読み込む
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 指定されたticket_idのデータを検索
        ticket_data = None
        for item in data.get('list', []):
            if item.get('ticket_id') == ticket_id:
                ticket_data = item
                break

        if not ticket_data:
            print(f"エラー: チケットID '{ticket_id}' がファイル '{json_file_path}' 内に見つかりませんでした。")
            return

        # --- 'schedules' の処理 ---
        schedules = ticket_data.get('schedules', [])
        if schedules:
            schedules_df = pd.json_normalize(schedules, sep='_')
            output_schedules_csv = f"{ticket_id}_schedules.csv"
            schedules_df.to_csv(output_schedules_csv, index=False, encoding='utf-8-sig')
            print(f"✅ '{output_schedules_csv}' が正常に作成されました。")
        else:
            print(f"情報: チケットID '{ticket_id}' に 'schedules' はありませんでした。")

        # --- 'event_schedules' の処理 ---
        event_schedules = ticket_data.get('event_schedules', [])
        if event_schedules:
            # 'event_summary' の改行コードをスペースに置換
            for event in event_schedules:
                if 'event_summary' in event and isinstance(event['event_summary'], str):
                    event['event_summary'] = event['event_summary'].replace('\n', ' ').replace('\r', ' ')
            
            event_schedules_df = pd.DataFrame(event_schedules)
            output_event_csv = f"{ticket_id}_event_schedules.csv"
            event_schedules_df.to_csv(output_event_csv, index=False, encoding='utf-8-sig')
            print(f"✅ '{output_event_csv}' が正常に作成されました。（改行コード置換済み）")
        else:
            print(f"情報: チケットID '{ticket_id}' に 'event_schedules' はありませんでした。")

    except FileNotFoundError:
        print(f"エラー: ファイル '{json_file_path}' が見つかりません。")
    except json.JSONDecodeError:
        print(f"エラー: ファイル '{json_file_path}' は有効なJSON形式ではありません。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")

if __name__ == '__main__':
    # コマンドライン引数をチェック
    if len(sys.argv) != 3:
        print("使い方: python json2csv.py <ファイル名.json> <チケットID>")
        print("例: python json2csv.py filename.json TICKETID")
        sys.exit(1) # エラーで終了

    # 引数を変数に格納
    file_name = sys.argv[1]
    target_ticket_id = sys.argv[2]
    
    # メインの処理関数を呼び出し
    process_ticket_data(file_name, target_ticket_id)
