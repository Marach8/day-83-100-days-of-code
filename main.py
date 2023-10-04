from flask import Flask, redirect, request 

marach = Flask(__name__, static_url_path='/static')

@marach.route('/')
def home():
  return "Welcome to My Blog's Homepage. Hope you are doing very fine?"


@marach.route('/story1', methods=['GET'])
def story1():
  title = 'Laptop'
  heading = "My Laptop Wahala"
  date = '17-05-2023'
  text = '''I went to Enugu yesterday to check my laptop baterry and all the man could do is to tell me that the battery he gave me initially had a seal in it while the one I am returning has no seal on it and therefore, there is nothing he can do about it. I nearly ran mad sha
  '''
  page1 = ''
  file = open('template/portfolio.html', 'r')
  page1 = file.read()
  file.close()
  page1 = page1.replace('{heading}', heading)
  page1 = page1.replace('{date}', date)
  page1 = page1.replace('{text}', text)
  page1 = page1.replace('{title1}', title)
  a = request.args
  if a == {}:
    page1 = page1.replace('{theme}', 'template/style.css')

  elif a['theme'] == 'blue':
    page1 = page1.replace('{theme}', 'template/blue.css')
  elif a['theme'] == 'green':
    page1 = page1.replace('{theme}', 'template/green.css')
  return page1

@marach.route('/story2', methods=['GET'])
def story2():
  title = 'Birthday'
  heading = 'Upcoming Birthday Tension'
  date = '22-05-1995'
  text = '''In a couple of days, I am going to officially be 28 years. All I can say is thanks be to Jesus christ, the author and finisher of our faith who in his infinite mercies has decided to keep me alive up to this day.
  I will be forever gratefull.
  '''
  page2 = ''
  file = open('template/portfolio.html', 'r')
  page2 = file.read()
  file.close()
  
  page2 = page2.replace('{heading}', heading)
  page2 = page2.replace('{date}', date)
  page2 = page2.replace('{text}', text)
  page2 = page2.replace('{title1}', title)
  a = request.args
  if a == {}:
    page2 = page2.replace('{theme}', 'template/style.css')
  elif a['theme'] == 'blue':
    page2 = page2.replace('{theme}', 'template/blue.css')
  elif a['theme'] == 'green':
    page2 = page2.replace('{theme}', 'template/green.css')
  
  return page2

@marach.route('/s2')
def direct():
  return redirect('https://day77100days--emmanuel2018.repl.co/story2')

@marach.route('/s1')
def direct2():
  return redirect('https://day77100days--emmanuel2018.repl.co/story1')

marach.run(host='0.0.0.0', port=81)