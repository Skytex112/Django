import datetime
from django.shortcuts import render

def show_page(request, page_number):

    pages = {
        "song": {
            "title": "Queen",
            "content": "We are the champions..."
        },
        "fr": {
            "title": "Reine",
            "content": "Nous sommes les champions..."
        },
        "de": {
            "title": "Königin",
            "content": "Wir sind die Champions..."
        },
        "es": {
            "title": "Reina",
            "content": "Somos los campeones..."
        },

        "home": {
            "title": "Головна",
            "content": "Про автомобілі"
        },
        "toyota": {
            "title": "Toyota",
            "content": "Надійні авто Toyota"
        },
        "honda": {
            "title": "Honda",
            "content": "Швидкі та економні авто"
        },
        "renault": {
            "title": "Renault",
            "content": "Французька якість"
        },

        "airpods": {
            "title": "AirPods",
            "content": "Apple wireless headphones"
        },
        "budslive": {
            "title": "Buds Live",
            "content": "Samsung headphones"
        },
    }
    if page_number == "day":
        days = ["Понеділок","Вівторок","Середа","Четвер","П'ятниця","Субота","Неділя"]

        images = {
            0: "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEhUSEhIVFRUVFxUXFxUXFxcYFRUXFxcXFxcVFxUYHSggGBolHRcVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDQ0NDg0NDisZFRk3Ny03Ny0rKzcrKzcrLSsrKy03KysrKysrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIALQBGAMBIgACEQEDEQH/xAAZAAEBAQEBAQAAAAAAAAAAAAABAgADBwT/xAApEAEBAAIABAUEAwEBAAAAAAAAAQIREjFR8CFBYXGBkaGx0QPh8cET/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAH/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwDxOQxoUDIoGA2i0g0DQ7aQ6BNxFxUqQERUa4tAN9m2dsAioIeL8Aq1V5JTll0FdNpyc+JUoJkP/m644CwHLTTFbZZCI4RVRqKiwWLTYInhGlaADSbFDQJCrBoEsaQMXpC5QbFUgVABZqDabKEiphh00EGXILsEgDFcwpwx83aiuWWKY631GWG+QOMOEPDXbWgc7Nf0qRWM7+TMQS1OcraQFw83Ox1xbSjlpOTrYi0HOwOmSKIkbNg0ABYBoWG0WgA1YFRcSoCqCGA2jowCiKjY1WgbFpzMVMQTwjS57trxBEn7dcfbv5MxXjjPZBymlbpuJk+wDi6xqcvT+voJPQHTHDZ4d+J/jnmudfEHz3HoJi7zH4F/j775g5ak76flzkrrlj9e/wBD7A5d91GUdcufJGSiE1ekUQCtWBNiVVIAVQBOmIBa45SrmQLjbRxK2Dpi2URhXSCjGKg8zaBOSdmA0XNeX+fTmJgrhBeM69+3oZNaqsLDkg58/TvYs1f+dfc5d/kS9+YE4+Hehrl3zXcffvroFYTv6ql0nC9dtby5gZlvkMvFeOHh63abPAHMaNs7vfezweGwc73XLJ29HPKd+YOdQvknKqiJGprbBNiVZQYwEirqaAoZgaRmipAEXExcAmUYtKDoIcaqiiYnQxVAMWhXF3/aC99/4Ze/NzVvvv4A2evRttL8f4eHX6oCa75um3O2/wCczvU8AdZ130V7d/CccfD1dfj0/YI4uXXv9pyP8iLn+QEynflerWiZpBVunHPuLmd6uWQIyopyTkqMmmpBVRyVW0CNptXpOUBDMwKim02wGlQRoC9iNWBWLpHPGkVc8Dvv9pyybG0Ha/dO+/L7id+qtINefPum8+/qJG3sHXGed/FTn4DeuV5L2CL7qxy8Of2924N9Dh7gvHWr53m6yxz6nK76/igvPxcM8fBVzFy38foEZDiaz0TkDZVzsVpOeSgyyc6qjIRqkgGZoAaoyXUAhjaAW2xsAZVxCgWMq0okBWKkYroC8ynSoBxydNuUXjRXXfNPg02dAq1pfEb+G2grGr1rvv0+sct/deN6gviTc9ecRll0Txd/0C7mNolMvwC+qa1TlQa5IyG2UGk2naRG2Ym0gU0ptBrU07RsGobbAzSplILhiTsFHaFApbmqUC2xaJQdMDajG+qoC8FSuW1yiq75NKmXq1yBV+q+LwcpDaBGfL6jZ0A22xDaBTlTRQTanbVhGyqa2SQUyaQbYYUE2g6AAggjaomGKE7ErILlO0RQKbYjAqFMXIDex2KmUHWZLnj6OeCtir4XOVVyTaCrk1qZRsRasYg40VVQeIZUGt7g2BsRqG2Ng1SbRsGDCgYnZ2Ng1SdpA1gwCFMKhUkoGKiIoDGtG2oKXMkKxoNYZAaC8aZk5ym0FStUbVKCsaKWtFG1RGVMoh220yMAqbVbTaDNRsAaGFoFNhGwahgDMwoBmZQEMCowbaCiloCmYwCqJMBZS2wbRlbZkBJjWNoGhEhoM0oVjQaRrWAJyDJAhtgDsbZgbaadigGIBhWCjEMAMDATGYGJYDDWZBePIVmAWqx8mYDkYzA2JhYBe/uIzAK22YCMmYEgMBFZgF5szAwZgFFZlAzMDVmYH//Z",
            1: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAA1BMVEUAVqp9mI3+AAAASElEQVR4nO3BgQAAAADDoPlTX+AIVQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwDcaiAAFXD1ujAAAAAElFTkSuQmCC",
            2: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASsAAACoCAMAAACPKThEAAAABlBMVEXmAALmAAEVGxVfAAAA50lEQVR4nO3UMQrEQAwEQfv/nzZMeJkxF2xTlQgEUtjXBX9y/8wXiy+3J34HOEaqvtoOaami6BXApOqr7QCTqq+2Q1qqKHoFMKn6ajvApOqr7ZCWKopeAUyqvtoOMKn6ajukpYqiVwCTqq+2A0yqvtoOaami6BXApOqr7QCTqq+2Q1qqKHoFMKn6ajvApOqr7ZCWKopeAUyqvtoOMKn6ajukpYqiVwCTqq+2A0yqvtoOaami6BXApOqr7QCTqq+2Q1qqKHoFMKn6ajvApOqr7ZCWKopeAUyqvtoOMKn6ajukpYqiV5zlAWpkBO0nZyv+AAAAAElFTkSuQmCC",
            3: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAA1BMVEX/zEgGqljXAAAASElEQVR4nO3BgQAAAADDoPlTX+AIVQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwDcaiAAFXD1ujAAAAAElFTkSuQmCC",
            4: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQMAAADCCAMAAAB6zFdcAAAABlBMVEX/mJn+m5pdqKetAAAAUUlEQVR4nO3QQREAAAzCMPBvejJ4LFHQa5rvHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFjrOmCuB082AAUUEDbiAAAAAElFTkSuQmCC",
            5: "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw0NDQgIDQ0HBwcIBw0HBwcHBw8ICQcNFREWFhURExMYHSggGBoxGxMTITEhJSkrLi4uFx8zODMsNygtLisBCgoKDQ0NDg0NDisZFRkrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIALcBEwMBIgACEQEDEQH/xAAYAAEBAQEBAAAAAAAAAAAAAAAAAQIHA//EABgQAQEBAQEAAAAAAAAAAAAAAAABEfAx/8QAFwEBAQEBAAAAAAAAAAAAAAAAAAEEA//EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AOqBBxaFVIogFAEUBFAAAAAAAAFBAAEUBBQEFAQUAABBUAZrSUVkAGhcAFQEUAAVAUAAAAUBAABQERQAABMUBBQEAAAARSgyUQVBFBsiLAUARFAACAoACgAAAAAAAigIAAAAAAigIAAADNRqoKyADUWIsBQBAAEUAUABUUAAAAAAAAAEAAAAARagAqAgoCMtJRWQ7xQVWVgNCKIAACgAAAKAgoIqACiAogAAACAoAIAAAAioAzWkFZ0AFWIsBVSKIAAoAAICiAKACiKAAAhUBUFAQAFQAVAAAEABEVBWVQBrFgAooIAoIKgAAAAKIoCgAioAipQBFAAAEUAAAABFQBKqUVkAG8IEBQBAACoAKigJGkAUAFEAVABAABAFABBUBRIoAACWKAyUQVAAbWICKAAgAAAsEAUFBFQBRAFBAKgAAAKiggqAAAoigAAiVWaKggD0AEUAERagqiKAAIogCiKBFQBUAEAABAUAAAFQAAAUTVBEq1misgINqixUAQAAUABRFERQAAAVFAoIAUQVRFEBFAEAURQAAAASpVqCsgA3FQAAAAAAAVARRAFEAUAAQAVAFAAAAQBVQBBdQBUAEQBWQAf/2Q==",
            6: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAA1BMVEUiiyKRpK8wAAAASElEQVR4nO3BgQAAAADDoPlTX+AIVQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwDcaiAAFXD1ujAAAAAElFTkSuQmCC"
        }

        i = datetime.datetime.today().weekday()

        return render(request, "index1.html", {
            "title": "День тижня",
            "content": days[i],
            "img": images[i]
        })

    page = pages.get(page_number, {
        "title": "Error",
        "content": "Page not found"
    })

    return render(request, 'index1.html', {'page': page})