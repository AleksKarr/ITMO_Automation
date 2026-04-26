# class Input:
#     def __init__(self, loc: str):
#         self.loc = loc
#
#
# search = Input("input#search")
# print(search.loc)


from task_9_cheks import Checks

class Input:
    def __init__(self, loc: str, text: str) -> None:
        self.loc = loc
        self.text = text


class Button:
    def __init__(self, loc: str, text: str) -> None:
        self.loc = loc
        self.text = text


class Title:
    def __init__(self, loc: str, text: str) -> None:
        self.loc = loc
        self.text = text


class Link:
    def __init__(self, loc: str, text: str) -> None:
        self.loc = loc
        self.text = text


search_input = Input("input#search", "Поиск")
submit_button = Button("button[type='submit']", "Отправить")
page_title = Title("h1.main-title", "Главная страница")
main_link = Link("a.home-link", "На главную")


print(search_input.text, search_input.loc)
print(submit_button.text, submit_button.loc)
print(page_title.text, page_title.loc)
print(main_link.text, main_link.loc)