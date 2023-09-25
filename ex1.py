from flask import Flask, render_template, request

app = Flask(__name__)


# Задание No1
# 📌 Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".
@app.route('/')
def index():
    return 'Hello, World!'


# Задание No2
# 📌 Дорабатываем задачу 1.
# 📌 Добавьте две дополнительные страницы в ваше веб-
# приложение:
# ○ страницу "about"
# ○ страницу "contact".
@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


# Задание No3
# 📌 Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.
@app.route('/sum/')
def summ():
    num_1 = int(request.args.get('num_1'))
    num_2 = int(request.args.get('num_2'))
    sum_two = num_1 + num_2
    context = {
        'num_1': str(num_1),
        'num_2': str(num_2),
        'sum': str(sum_two)
    }
    return render_template('sum.html', **context)


# Задание No4
# 📌 Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.
@app.route('/length/')
def length():
    line = request.args.get('line')
    length_line = len(line)
    context = {
        'title': 'Length of the line',
        'line': line,
        'length': length_line
    }
    return render_template('length.html', **context)


# Задание No5
# 📌 Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".
@app.route('/first/')
def first():
    context = {
        'title': 'My first HTML page!',
        'content': 'Hello, world!'
    }
    return render_template('first.html', **context)


# Задание No6
# 📌 Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# 📌 Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# 📌 Данные о студентах должны быть переданы в шаблон через контекст.
@app.route('/students/')
def students():
    _students_list = [
        {'name': 'Anton', 'surname': 'Antonov', 'age': 34, 'average': 4},
        {'name': 'Harry', 'surname': 'Dirty', 'age': 40, 'average': 5},
        {'name': 'Wesly', 'surname': 'Snipes', 'age': 50, 'average': 2},
        {'name': 'Tom', 'surname': 'Whisley', 'age': 30, 'average': 3},
        {'name': 'Ioghan', 'surname': 'Bach', 'age': 60, 'average': 4},
    ]
    context = {
        'students': _students_list,
        'title': 'Students'
    }
    return render_template('students.html', **context)


# Задание No7
# 📌 Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# 📌 Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# 📌 Данные о новостях должны быть переданы в шаблон через контекст.
@app.route('/news/')
def news():
    _news = [
        {'title': 'Deforestation', 'excerpt': 'The area of forest are in decline', 'date': '12.05.2004'},
        {'title': 'Record inflation', 'excerpt': 'The inflation reached 100% in Argentina', 'date': '25.11.2014'},
        {'title': 'Global warming', 'excerpt': 'Scientists can not find prove of global warming', 'date': '01.01.1999'}
    ]
    context = {
        'newses': _news,
        'title': 'Global news'
    }
    return render_template('news.html', **context)


# Задание No8
# 📌 Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна
# (шапка, меню, подвал), и дочерние шаблоны для каждой отдельной страницы.
# 📌 Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.
@app.route('/contact/')
def contactbase():
    return render_template('contact.html')


@app.route('/aboutus/')
def about_us():
    return render_template('about-us.html')


# Задание No9
# 📌 Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# 📌 Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.
@app.route('/clothing/')
def clothing():
    return render_template('clothing.html')


@app.route('/electronics/')
def electronics():
    return render_template('electronics.html')


@app.route('/food/')
def food():
    return render_template('food.html')


if __name__ == '__main__':
    app.run(debug=True)
