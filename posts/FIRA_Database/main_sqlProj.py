import pymysql
import pymysql.cursors

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    
print('''
============================================================
1. print all buildings
2. print all performances
3. print all audiences
4. insert a new building
5. remove a building
6. insert a new performance
7. remove a performance
8. insert a new audience
9. remove an audience
10. assign a performance to a building
11. book a performance
12. print all performances assigned to a building
13. print all audiences who booked for a performance
14. print ticket booking status of a performance
15. exit
============================================================
''')

order = eval(input("Select your action: "))

while order != 15:
    if order == 1:
        
        # 1. Print all buildings

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:
                # Select records from buildings table
                sql = "SELECT id, name, location, capacity, assigned FROM buildings"
                cursor.execute(sql)
                result = cursor.fetchall()
                print('- ' * 42)
                print('id'.ljust(10) + 'name'.ljust(35) + 'location'.ljust(15) + 'capacity'.ljust(15) + 'assigned'.ljust(15))
                print('- ' * 42)
                
                if len(result) != 0:
                    for i in range(len(result)):
                        print( ('%d' % result[i][0]).ljust(10) +
                              ('%s' % result[i][1]).ljust(35) +
                              ('%s' % result[i][2]).ljust(15) +
                              ('%d' % result[i][3]).ljust(15) +
                              ('%d' % result[i][4]).ljust(15) )
                        
                    print('- ' * 42)
                
        finally:
            connection.close()

    elif order == 2:
        # 2. Print all performances

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:
                # Select records from performances table
                sql = "SELECT id, name, type, price, booked FROM performances"
                cursor.execute(sql)
                result = cursor.fetchall()
                print('- ' * 42)
                print('id'.ljust(10) + 'name'.ljust(35) + 'type'.ljust(15) + 'price'.ljust(15) + 'booked'.ljust(15))
                print('- ' * 42)
                
                if len(result) != 0:
                    for i in range(len(result)):
                        print( ('%d' % result[i][0]).ljust(10) +
                              ('%s' % result[i][1]).ljust(35) +
                              ('%s' % result[i][2]).ljust(15) +
                              ('%d' % result[i][3]).ljust(15) +
                              ('%d' % result[i][4]).ljust(15) )      
                        
                    print('- ' * 42)
                    
        finally:
            connection.close()

    elif order == 3:

        # 3. Print all audiences

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:
                # Select records from audiences table
                sql = "SELECT id, name, gender, age FROM audiences"
                cursor.execute(sql)
                result = cursor.fetchall()
                print('- ' * 33)
                print( 'id'.ljust(10) + 'name'.ljust(35) + 'gender'.ljust(15) + 'age'.ljust(15) )
                print('- ' * 33)
                
                if len(result) != 0:
                    for i in range(len(result)):
                        print( ('%d' % result[i][0]).ljust(10) +
                              ('%s' % result[i][1]).ljust(35) +
                              ('%s' % result[i][2]).ljust(15) +
                              ('%d' % result[i][3]).ljust(15) )
                        
                    print('- ' * 33)
                
        finally:
            connection.close()

    elif order == 4:
        
        # 4. Insert a new building

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:
                # INSERT INTO a new building records
                b_name = input("Builidng name: ")
                b_location = input("Building location: ")
                b_capacity = input("Building capacity: ")
                
                if eval(b_capacity) > 999999999:
                    raise MyError("범위를 벗어난 숫자를 입력하였습니다.")
                
                sql = "INSERT INTO buildings (name, location, capacity) VALUES('%s', '%s', %d)" % (b_name[:200], b_location[:200], eval(b_capacity))
                cursor.execute(sql)
                connection.commit()
                print("A building is successfully inserted")
                
        except MyError as e:
            print(e)
                
        finally:
            connection.close()

    elif order == 5:
        
        # 5. Remove a building

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:
                
                # Building ID validator
                sql1 = "SELECT id FROM buildings"
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                lst1 = []
                for i in range(len(result1)):
                    lst1 += [result1[i][0]]
                    
                b_id = eval( input("Building ID: ") )
                
                if b_id not in lst1:
                    raise MyError("ERROR : 해당 번호를 가진 공연장이 없습니다.")
                    
                # Search a performance ID which the building is assigned to
                sql2 = "SELECT id FROM performances WHERE b_id = %d" % (b_id)
                cursor.execute(sql2)
                result2 = cursor.fetchall()
                if result2 == ():
                    p_id = result2
                else:
                    tuple2 = ()
                    for i in range(len(result2)):
                        tuple2 += result2[i]
                        
                    p_id = str(tuple2)
                    
                    if len(tuple2) == 1:
                        p_id = '(%d)' % (tuple2[0])
                
                # Update performance records
                if p_id != ():
                    sql3 = "UPDATE performances SET b_id = Null WHERE id in %s" % (p_id)
                    sql3a = "UPDATE performances SET booked = 0 WHERE id in %s" % (p_id)
                    cursor.execute(sql3)
                    cursor.execute(sql3a)
                    connection.commit()
                
                    # Delete records from book
                    sql4 = "DELETE FROM book WHERE p_id in %s" % (p_id)
                    cursor.execute(sql4)
                    connection.commit()
                
                # Delete records from buildings
                sql5 = "DELETE FROM buildings WHERE ID = %d" % (b_id)
                cursor.execute(sql5)
                connection.commit()       

                print("A building is successfully removed")
                
        except MyError as e:
            print(e)
                
        finally:
            connection.close()

    elif order == 6:

        # 6. INSERT INTO a new performance records

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:

                p_name = input("Performance name: ")
                p_type = input("Performance type: ")
                p_price = input("Performance price: ")

                if eval(p_price) > 999999999:
                    raise MyError("범위를 벗어난 숫자를 입력하였습니다.")

                sql = "INSERT INTO performances (name, type, price) VALUES('%s', '%s', %d)" % (p_name[:200], p_type[:200], eval(p_price))
                cursor.execute(sql)
                connection.commit()
                print("A performance is successfully inserted")

        except MyError as e:
            print(e)

        finally:
            connection.close()

    elif order == 7:
        # 7. Remove a performance

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:

                # Performance ID validator
                sql1 = "SELECT id FROM performances"
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                lst1 = []
                for i in range(len(result1)):
                    lst1 += [result1[i][0]]
                    
                p_id = eval( input("Performance ID: ") )
                if p_id not in lst1:
                    raise MyError("ERROR : 해당 번호를 가진 공연이 없습니다.")
                    
                # Search building ID which performance is assigned
                sql2 = "SELECT b_id FROM performances WHERE id = %d" % (p_id)
                cursor.execute(sql2)
                result2 = cursor.fetchall()
                b_id = result2[0][0]
                
                # Remove a performance
                sql3 = "DELETE FROM performances WHERE id = %d" % (p_id) 
                cursor.execute(sql3)
                connection.commit()
                
                # Updating building's assigned number
                if b_id != None:
                    sql4 = "UPDATE buildings SET assigned = (SELECT COUNT(b_id) FROM performances WHERE b_id = %d) WHERE id = %d" % (b_id, b_id)
                    cursor.execute(sql4)
                    connection.commit()
                    
                print("A performance is successfully removed")            
                    
        except MyError as e:
            print(e)
                
        finally:
            connection.close()

    elif order == 8:
        
        # 8. INSERT a new audience records

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:
                a_name = input("Audience name: ")
                a_gender = input("Audience gender: ")
                a_age = input("Audience age: ")
                
                if eval(a_age) > 200:
                    raise MyError("범위를 벗어난 숫자를 입력하였습니다.")
                
                sql = "INSERT INTO audiences (name, gender, age) VALUES('%s', '%s', %d)" % (a_name[:200], a_gender, eval(a_age))
                cursor.execute(sql)
                connection.commit()
                print("An audience is successfully inserted")
                
        except MyError as e:
            print(e)
                
        finally:
            connection.close()

    elif order == 9:
        # 9. Remove an audience

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:

                # Audience ID validator
                sql1 = "SELECT id FROM audiences"
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                lst1 = []
                for j in range(len(result1)):
                    lst1 += [result1[j][0]]
                    
                a_id = eval( input("Audience ID: ") )        
                if a_id not in lst1:
                    raise MyError("ERROR : 해당 번호를 가진 회원이 없습니다.")

                # Remove an audience
                sql2 = "DELETE FROM audiences WHERE id = %d" % (a_id) 
                cursor.execute(sql2)
                connection.commit()
                print("An audience is successfully removed")
                    
        except MyError as e:
            print(e)
                
        finally:
            connection.close()

    elif order == 10:
        
        # 10. assign a performance to a building

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:
                
                # Building ID validator
                sql1 = "SELECT id FROM buildings"
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                lst1 = []
                for i in range(len(result1)):
                    lst1 += [result1[i][0]]
                b_id = eval( input("Building ID: ") )
                if b_id not in lst1:
                    raise MyError("ERROR : 해당 번호를 가진 공연장이 없습니다.")
                
                # Performance ID validator
                sql2 = "SELECT id FROM performances"
                cursor.execute(sql2)
                result2 = cursor.fetchall()
                lst2 = []
                for i in range(len(result2)):
                    lst2 += [result2[i][0]]
                p_id = eval( input("Performance ID: ") )
                if p_id not in lst2:
                    raise MyError("ERROR : 해당 번호를 가진 공연이 없습니다.")
                
                # Checking the Performance ID was already assigned.
                sql3 = "SELECT b_id FROM performances WHERE id = %d" % (p_id)
                cursor.execute(sql3)
                result3 = cursor.fetchall()
                
                if result3[0][0] != None:
                    raise MyError("ERROR : 해당 공연이 이미 다른 공연장에 배정되어 있습니다.")
                
                # Update assign bilding ID in performance table
                sql4 = "UPDATE performances SET b_id = %d WHERE id = %d" % (b_id, p_id)
                cursor.execute(sql4)
                connection.commit()
                print("Successfully assigned a performance")

                # Updating building's assigned number           
                sql5 = "UPDATE buildings SET assigned = (SELECT COUNT(b_id) FROM performances WHERE b_id = %d) WHERE id = %d" % (b_id, b_id)
                cursor.execute(sql5)
                connection.commit()

                    
        except MyError as e:
            print(e)
                
        finally:
            connection.close()

    elif order == 11:

        # 11. Book a performance

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:
                
                # Performance ID validator
                sql1 = "SELECT id FROM performances"
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                lst1 = []
                for i in range(len(result1)):
                    lst1 += [result1[i][0]]
                    
                p_id = eval( input("Performance ID: ") )
                sql1a = "SELECT b_id FROM performances WHERE id = %d" % (p_id)
                cursor.execute(sql1a)
                result1a = cursor.fetchall()
                
                if p_id not in lst1:
                    raise MyError("ERROR : 해당 번호를 가진 공연이 없습니다.")
                    
                if result1a[0][0] == None:
                    raise MyError("ERROR : 해당 공연은 아직 공연장이 배정되지 않았습니다.")

                # Audience ID validator
                sql2 = "SELECT id FROM audiences"
                cursor.execute(sql2)
                result2 = cursor.fetchall()
                lst2 = []
                for j in range(len(result2)):
                    lst2 += [result2[j][0]]
                    
                a_id = eval( input("Audience ID: ") )        
                if a_id not in lst2:
                    raise MyError("ERROR : 해당 번호를 가진 회원이 없습니다.")
         

                # Seat number validator
                sql3 = "SELECT p_id, seat_num FROM (book JOIN performances p ON p.id = book.p_id) JOIN buildings b ON p.b_id = b.id WHERE p_id = %d" % (p_id)
                cursor.execute(sql3)
                result3 = cursor.fetchall()
                lst3 = []
                
                for k in range(len(result3)):
                    if type(eval(result3[k][1])) == int:                
                        lst3 += [eval(result3[k][1])]
                    else:
                        lst3 += list(eval(result3[k][1]))
                
                seat_num = input("Seat number: ")
                if type(eval(seat_num)) == int:
                    seat_nums = {eval(seat_num)}
                else:
                    seat_nums = {*eval(seat_num)}

                if set(lst3) - seat_nums != set(lst3):
                    raise MyError("ERROR : 이미 예약된 좌석 번호가 포함되어 있습니다.")
                
                sql4 = "SELECT capacity FROM performances p JOIN buildings b ON p.b_id = b.id WHERE p.id = %d" % (p_id)
                cursor.execute(sql4)
                result4 = cursor.fetchall()
                
                if max(seat_nums) > result4[0][0]:
                    raise MyError("ERROR : 존재하지 않는 좌석 번호가 포함되어 있습니다.")
                    
                
                # Book a seat_num - insert into book-table a record
                sql5 = "INSERT INTO book (a_id, p_id, seat_num) VALUES (%d, %d, '%s')" % (a_id, p_id, seat_num)
                cursor.execute(sql5)
                connection.commit()

                # Updating number of booked in performances table
                NumOfBooking = len(seat_nums)
                sql6 = "SELECT booked, price FROM performances WHERE id = %d" % (p_id)
                cursor.execute(sql6)
                result6 = cursor.fetchall()
                
                sql7 = "UPDATE performances SET booked = %d WHERE id = %d" % (result6[0][0] + NumOfBooking, p_id)
                cursor.execute(sql7)
                connection.commit()
                print("Successfully booked a performance")
                print("Total ticket price is %d" % (NumOfBooking * result6[0][1]))
                
                
        except MyError as e:
            print(e)
                
        finally:
            connection.close()

    elif order == 12:

        # 12. print all performances assigned to a buildings

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:
                
                # Building ID validator
                sql1 = "SELECT id FROM buildings"
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                lst1 = []
                for i in range(len(result1)):
                    lst1 += [result1[i][0]]
                b_id = eval( input("Building ID: ") )
                
                if b_id not in lst1:
                    raise MyError("ERROR : 해당 번호를 가진 공연장이 없습니다.")
                
                # Show performances information assigned to building id.
                sql = "SELECT id, name, type, price, booked FROM performances WHERE b_id = %d" % (b_id)
                cursor.execute(sql)
                result = cursor.fetchall()
                print('- ' * 42)
                print('id'.ljust(10) + 'name'.ljust(35) + 'type'.ljust(15) + 'price'.ljust(15) + 'booked'.ljust(15))
                print('- ' * 42)
                if len(result) != 0:
                    for i in range(len(result)):
                        print( ('%d' % result[i][0]).ljust(10) +
                              ('%s' % result[i][1]).ljust(35) +
                              ('%s' % result[i][2]).ljust(15) +
                              ('%d' % result[i][3]).ljust(15) +
                              ('%d' % result[i][4]).ljust(15) )
                        
        except MyError as e:
            print(e)
                
        finally:
            connection.close()

    elif order == 13:

        # 13. print all audiences who booked for a performance

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:

                # Performance ID validator
                sql1 = "SELECT id FROM performances"
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                lst1 = []
                for i in range(len(result1)):
                    lst1 += [result1[i][0]]
                    
                p_id = eval( input("Performance ID: ") )
                sql1a = "SELECT b_id FROM performances WHERE id = %d" % (p_id)
                cursor.execute(sql1a)
                result1a = cursor.fetchall()
                
                if p_id not in lst1:
                    raise MyError("ERROR : 해당 번호를 가진 공연이 없습니다.")
                    
                if result1a[0][0] == None:
                    raise MyError("ERROR : 해당 공연은 아직 공연장이 배정되지 않았습니다.")

                # Select records from audiences JOIN book table        
                sql2 = "SELECT DISTINCT a.id, a.name, a.gender, a.age FROM book b JOIN audiences a ON b.a_id = a.id WHERE b.p_id = %d" % (p_id)
                cursor.execute(sql2)
                result = cursor.fetchall()
                print('- ' * 33)
                print( 'id'.ljust(10) + 'name'.ljust(35) + 'gender'.ljust(15) + 'age'.ljust(15) )
                print('- ' * 33)
                if len(result) != 0:
                    for i in range(len(result)):
                        print( ('%d' % result[i][0]).ljust(10) +
                              ('%s' % result[i][1]).ljust(35) +
                              ('%s' % result[i][2]).ljust(15) +
                              ('%d' % result[i][3]).ljust(15) )
                print('- ' * 33)

        except MyError as e:
            print(e)
                
        finally:
            connection.close()

    elif order == 14:

        # 14. print ticket booking status of a performance

        connection = pymysql.connect(
            host = 'astronaut.snu.ac.kr',
            user = 'BDE-2018-16',
            password = '3abe759220a4',
            db = 'BDE-2018-16',
            charset = 'utf8',
            cursorclass = pymysql.cursors.Cursor
        )

        try:
            with connection.cursor() as cursor:

                # Performance ID validator
                sql1 = "SELECT id FROM performances"
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                lst1 = []
                for i in range(len(result1)):
                    lst1 += [result1[i][0]]
                    
                p_id = eval( input("Performance ID: ") )
                sql1a = "SELECT b_id FROM performances WHERE id = %d" % (p_id)
                cursor.execute(sql1a)
                result1a = cursor.fetchall()
                
                if p_id not in lst1:
                    raise MyError("ERROR : 해당 번호를 가진 공연이 없습니다.")
                    
                if result1a[0][0] == None:
                    raise MyError("ERROR : 해당 공연은 아직 공연장이 배정되지 않았습니다.")

                # Making booking status        
                sql2 = "SELECT capacity FROM buildings b JOIN performances p ON b.id = p.b_id WHERE p.id = %d" % (p_id)
                cursor.execute(sql2)
                result2 = cursor.fetchall()
                
                sql3 = "SELECT b.a_id, b.seat_num FROM book b WHERE p_id = %d" % (p_id)
                cursor.execute(sql3)
                result3 = cursor.fetchall()
                
                print('- ' * 40)
                print( 'seat_number'.ljust(40) + 'audience_id'.ljust(40) )
                print('- ' * 40)
                
                for i in range(result2[0][0]):
                    count = 0
                    for j in range(len(result3)):
                        if type(eval(result3[j][1])) == int:
                            if i + 1 in [eval(result3[j][1])]:
                                print( ('%d' % (i+1)).ljust(40) + ('%d' % result3[j][0]).ljust(40) )
                                count += 1
                        else:
                            if i + 1 in [*eval(result3[j][1])]:
                                print( ('%d' % (i+1)).ljust(40) + ('%d' % result3[j][0]).ljust(40) )
                                count += 1
                    if count == 0:
                        print( ('%d' % (i+1)).ljust(40) )
                                            
                print('- ' * 40)

        except MyError as e:
            print(e)
                
        finally:
            connection.close()

    elif order == 15:
        print("Bye!")
        exit()

    print()
    order = eval(input("Select your action: "))
