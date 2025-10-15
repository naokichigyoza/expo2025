# expo2025 過去の入場履歴・パビリオンとイベント予約の履歴成形ツール

1. 以下にログイン
https://ticket.expo2025.or.jp/

2. 以下のjsonを任意の名前で保存（例：output.json）
https://ticket.expo2025.or.jp/api/d/my/tickets/?count=1

3. 同じフォルダに「json2csv.py」を配置

4. jsonのファイル名とチケットIDを引数にpythonを実行
   python json2csv.py output.json *TICKETID*

5. ファイル生成完了
   入場予約：チケットID_schedules.csv
   パビリオンとイベント予約：チケットID_event_schedules.csv
