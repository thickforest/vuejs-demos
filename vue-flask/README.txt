(1) 初始化数据库
./manager.py db init
./manager.py db migrate
./manager.py db upgrade

(2) 运行
./manager.py runserver -h 0.0.0.0 -p 5000 -d
