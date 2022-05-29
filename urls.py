from datetime import date

from views import (Another_page, CategoryList, Contact, CopyCourse,
                   CoursesList, CreateCategory, CreateCourse, Examples, Index)


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/index/': Index(),
    '/contact/': Contact(),
    '/page/': CreateCategory(),
    '/another_page/': CoursesList(),
    '/examples/': Examples(),
    '/create_course/': CreateCourse(),
    '/category_list/': CategoryList(),
    '/copy-course/': CopyCourse()
}
