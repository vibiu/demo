#After you enter demo

## platform: ubuntu 16.04-64bit

## the use of sqlite3 && c
### prepare
    //install sqlite3
    sudo apt install sqlite3

    //install sqlite3 develop library
    sudo apt install libsqlite3-dev

### init
    // create database engine
    sqlite3 test.db

### connect
    code: sqlite3democ.c

    //gcc compile
    gcc sqlite3democ.c -l sqlite3 -o connect
    
    //execute
    ./connect

### result
you'll see "Opened database successfully" in the screan

see [Installing sqlite headers on ubuntu](http://www.databasically.com/2010/03/05/installing-sqlite-headers-on-ubuntu-sqlite3-h-not-found/)

see [An Introduction To The SQLite C/C++ Interface](https://www.sqlite.org/cintro.html)

see [RUNOOB.COM SQLite-c/c++](http://www.runoob.com/sqlite/sqlite-c-cpp.html)

## the use of mysql && c
## prepare
    //install mysql-server
    sudo apt install mysql-server mysql-client

    //install mysql-develop
    sudo apt install libmysqlclient-dev

## connect
    code: mysqldemoc.c

    //gcc compile
    gcc -o mysqldemoc mysqldemoc.c `mysql_config --cflags --libs`

    //execute
    ./mysqldemoc

## result
you'll see:

    MySQL Tables in mysql database:
    columns_priv 
    db 
    engine_cost 
    event 
    ...

see [How to install mysql server 5.7 on Ubuntu 16.04 LTS](http://www.cyberciti.biz/faq/howto-install-mysql-on-ubuntu-linux-16-04/)

see [mysql.h file can't be found](http://stackoverflow.com/questions/14604228/mysql-h-file-cant-be-found)

see [undefined reference to mysql_init?](http://ubuntuforums.org/showthread.php?t=1666018)

see [MySQL C API programming tutorial](http://zetcode.com/db/mysqlc/)
