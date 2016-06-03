// #include <stdio.h>
// #include <mysql/mysql.h>

/* Simple C program that connects to MySQL Database server*/
// #include "/usr/include/mysql/my_global.h"
// #include "/usr/include/mysql/mysql.h"
// #include "mysql/my_global.h"
// #include "mysql/mysql.h"

#include <my_global.h>
#include <mysql.h>
#include <stdio.h>
int main() {
   MYSQL *conn;
   MYSQL_RES *res;
   MYSQL_ROW row;
   char *server = "localhost";
   char *user = "root";
   char *password = "password"; /* set me first */
   char *database = "mysql";
   conn = mysql_init(NULL);
   /* Connect to database */
   if (!mysql_real_connect(conn, server,
         user, password, database, 0, NULL, 0)) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      exit(1);
   }
   /* send SQL query */
   if (mysql_query(conn, "show tables")) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      exit(1);
   }
   res = mysql_use_result(conn);
   /* output table name */
   printf("MySQL Tables in mysql database:\n");
   while ((row = mysql_fetch_row(res)) != NULL)
      printf("%s \n", row[0]);
   /* close connection */
   mysql_free_result(res);
   mysql_close(conn);
}

// /*another demo*/
// int main(int argc, char **argv)
// {  
//   MYSQL *con = mysql_init(NULL);

//   if (con == NULL) 
//   {
//       printf("%s\n", mysql_error(con));
//       exit(1);
//   }else{
//     printf("ok\n");
//   }

//   if (mysql_real_connect(con, "localhost", "root", "274058", 
//           NULL, 0, NULL, 0) == NULL) 
//   {
//       fprintf(stderr, "%s\n", mysql_error(con));
//       mysql_close(con);
//       exit(1);
//   }  

//   if (mysql_query(con, "CREATE DATABASE testdb")) 
//   {
//       fprintf(stderr, "%s\n", mysql_error(con));
//       mysql_close(con);
//       exit(1);
//   }

//   mysql_close(con);
//   exit(0);
// }
