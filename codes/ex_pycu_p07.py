def show_line():
    n = 80
    t = '-'
    print(t * n)


def show_description(text):
    show_line()
    print(text)


def sec_summation():
    problem = "Count seconds from time in the format h:m:s"
    show_description(problem)
    x = input('Enter time (3 values of h m s): ')
    t = x.split()
    s = int(t[0])*60*60 + int(t[1])*60 + int(t[2])
    print(f'{t[0]}h:{t[1]}m:{t[2]}s = {s} seconds.')
    show_line()


def calculate_y():
    problem = "Calculate y = 2 - x + (3/7)x^2 - (5/11)x^3"
    show_description(problem)
    x = float(input('Enter a real number x = '))
    y = 2 - x + (3/7)*(x**2) - (5/11)*(x**3)
    print(f'y = 2 - ({x}) + (3/7)*({x})^2 - (5/11)*({x})^3 = {y}')
    show_line()


def iteration_4_times():
    problem = "Do an iteration 4 times"
    show_description(problem)
    a = float(input('Enter a real number: '))
    x = 1
    c = 0
    print(f'ROUND {c}: x = {x}')
    while c < 4:
        x = (x + a/x)/2
        c = c + 1
        print(f'ROUND {c}: x = ( ({x}) + ({a})/({x}) ) / 2 = {x}')
    show_line()


def vectors():
    problem = "3d-Vector norm and dot product"
    show_description(problem)
    v = input('Vector v: ')
    u = input('Vector u: ')
    v = v.split()
    u = u.split()
    norm_v = (float(v[0])**2 + float(v[1])**2 + float(v[2])**2)**0.5
    norm_u = (float(u[0]) ** 2 + float(u[1]) ** 2 + float(u[2]) ** 2)**0.5
    dp = float(v[0])*float(u[0]) + float(v[1])*float(u[1]) + float(v[2])*float(u[2])
    print(f'Norm(v) = {norm_v}')
    print(f'Norm(u) = {norm_u}')
    print(f'v dot u = {dp}')
    show_line()


def distance2d():
    problem = "2d-Euclidean distance"
    show_description(problem)
    a = input('Point (x_1, y_1): ')
    b = input('Point (x_2, y_2): ')
    a = a.split()
    b = b.split()
    d = ((float(a[0]) - float(b[0]))**2 + (float(a[1]) - float(b[1]))**2)**0.5
    print(f'Distance between {(float(a[0]), float(a[1]))} and {(float(b[0]), float(b[1]))} is {d}')
    show_line()


def average():
    problem = "Average value"
    show_description(problem)
    x = input('Enter 5 numbers: ')
    x = x.split()
    avg = (float(x[0]) + float(x[1]) + float(x[2]) + float(x[3]) + float(x[4]))/5
    print(f'Average = {avg}')
    show_line()


def maketext():
    problem = "Make text"
    show_description(problem)
    x = input('Enter 3 inputs (2 characters and 1 integer): ')
    x = x.split()
    y = x[0] + x[1] + x[2] + (x[0] + x[1])*int(x[2])
    print(f'New text is {y}')


# Main
run = 1
while run == 1:
    choice = int(input('Choose problem number (1-9, 0 to exit): '))
    if choice == 1:
        sec_summation()
    elif choice == 2:
        calculate_y()
    elif choice == 3:
        iteration_4_times()
    elif choice == 4:
        vectors()
    elif choice == 5:
        distance2d()
    elif choice == 6:
        print('Not done yet.')
    elif choice == 7:
        print('Not done yet')
    elif choice == 8:
        average()
    elif choice == 9:
        maketext()
    else:
        run = 0
        print('Exit')
