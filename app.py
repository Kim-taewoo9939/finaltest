from flask import Flask, render_template, request, session, redirect
import bdb # 내가 만든 데이터베이스 함수들

app = Flask(__name__)
app.secret_key = b'aaa!111/'


@app.route('/')
def index():
    return render_template("main.html")

@app.route('/hello')
def hello():
    return render_template("main.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        # 여기 POST로 들어오는 데이터를 받아보자
        id = request.form['id']
        pwd = request.form['pwd']
        print("전달된값:", id, pwd)
        # 만약에 이메일과 패스워드 같다면
        if id == 'a@a.com' and pwd == '1234':
        #ret = bdb.get_idpw(id, pwd)
        #print(ret)
        # 로그인 성공
        #if ret != 'None':
            session['id'] = id
            return "로그인 성공"
        # 아니면
        else:
        # 아이디 패스워드 확인
            return "아이디 패스워드 확인"

# 로그아웃(session 제거)
@app.route('/logout')
def logout():
    session.pop('uesr', None)
    return redirect('form')
    # 로그인 사용자만 접근 가능으로 만들면 
@app.route('/form') 
def form(): 
    if 'user' in session: 
        return render_template('test.html') 
    return redirect(('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return "GET으로 전송이다"
    else:
        # 여기 POST로 들어오는 데이터를 받아보자
        num = request.form['num']
        name = request.form['name']
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/naver')
def naver():
    if 'email' in session:   # 로그인 상태값(세션) 체크
        return render_template("naver.html")  # 네이버 검색 페이지 사용
    else:
        return redirect('/login')  # 로그인 페이지로 강제 이동





if __name__ == '__main__':
    app.run()