import web
render = web.template.render('templates/')
movies = [
	{
		'title': 'Forrest Gump',
		'year': 1994,
	},
	{
		'title': 'Titanic',
		'year':	1997,
	},
]
urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return render.index(movies)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()