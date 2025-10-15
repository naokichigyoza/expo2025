# 大阪・関西万博　過去予約の履歴成形ツール

1. 以下にログイン
   
   https://ticket.expo2025.or.jp/

3. 以下のjsonを任意の名前で保存（例：output.json）
   
   https://ticket.expo2025.or.jp/api/d/my/tickets/?count=1

5. 同じフォルダに「json2csv.py」を配置

6. jsonのファイル名とチケットIDを引数にpythonを実行
   （例：python json2csv.py output.json <チケットID>）

8. ファイル生成完了
   
   入場予約：<チケットID>_schedules.csv
   
   パビリオンとイベント予約：<チケットID>_event_schedules.csv
