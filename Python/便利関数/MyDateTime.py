import datetime

def get_firstday_week(day_dt=datetime.date.today(),mode="sun") -> str:
    """
    - 指定日の週の開始日を文字列(yyyy-mm-dd)で返す
    - modeを"mon"に変更すると週の開始日を月曜日に変更できます。
    """
    # 曜日との差分を取得
    _weekday_first = 0 - day_dt.weekday()

    # 日にちに変換
    if _weekday_first == -6:
        _mon_fist_date = day_dt
    elif mode == "sun":
        _mon_fist_date = day_dt + datetime.timedelta(days=_weekday_first-1)
    elif mode == "":
        _mon_fist_date = day_dt + datetime.timedelta(days=_weekday_first)

    return _mon_fist_date.strftime("%Y-%m-%d")