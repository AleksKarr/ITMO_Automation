class Button:


    def     __init__(self, text, link):
        self.text   = text
        self.link   = link

# Cоздаем экземпляры класса
home    = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

#Получаем доступ к атрибутам
print(home.text)
print('Кнопка'  +home.text + 'имеет ссылку' + home.link)

print('/n')

print(catalog_msk.text)
print('Кнопка' + catalog_msk.text + 'имеет ссылку' + catalog_msk.link)
import urllib



class ButtonTwo:


    def     __init__(self, text, link, loc):
        self.text   = text
        self.link   = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.text)


# Cоздаем экземпляры класса
homeTwo    = ButtonTwo('Домой', '/home', 'button#home')

# Вызываем метод
print(homeTwo.click())

class Input:

    def __init__(self, loc):
        self.loc = loc


search = Input('input#search')

print(search.loc)


