from django.shortcuts import render
import datetime
from django.http import HttpResponse

def current_datetime(request):
    import datetime
    now = datetime.datetime.now()

    return HttpResponse(f"""
        <h1>Current date and time</h1>
        <p>{now}</p>
    """)

def multiplication_table(request):
    content = """
    <h1>Multiplication Table</h1>
    <table border="1">
    """

    for i in range(1, 11):
        content += "<tr>"
        for j in range(1, 11):
            content += f"<td>{i*j}</td>"
        content += "</tr>"

    content += "</table>"

    return HttpResponse(content)

def programmer_day(request):
    import datetime

    year = datetime.datetime.now().year
    day = datetime.datetime(year, 1, 1) + datetime.timedelta(days=255)

    return HttpResponse(f"""
        <h1>Programmer Day</h1>
        <p>Year: {year}</p>
        <p>Date: {day.date()}</p>
    """)