def menu(request):
    return {
        "menu_items": [
            {"menu_name": "Главная", "menu_url": "home"},
            {"menu_name": "Блог", "menu_url": "blog"},
            {"menu_name": "О нас", "menu_url": "about"},
        ]
    }
