import matplotlib
import matplotlib.pyplot as plt

# Cuando es DDA PARA EL CUADRADO.

def main():
    # SELECCIONAR EL ALGORITMO
    tipo = int(
        input("ALGORITMOS..\n1.DDA \n2.Bresenhams \nSelecciona un algoritmo: "))
    # OPCION DDA
    if tipo == 1:
        print("DDA")
        cuantos = int(input(
                "\nSelecciona uno.\n1.Cuadrado\n2.Rectangulo\n3.Triangulo \n4.triangulo rectangulo\nCon que figura quieres trabajar: "))
    if tipo == 1:
            f1 = plt.figure(1).add_subplot(1,1,1)
            plt.title("Algoritmo DDA")
            plt.grid()

            if tipo == 1 and cuantos == 1 or cuantos == 2:
                X1=3
                Y1=2
                X2=3
                Y2=6

            if tipo == 1 and cuantos == 3 :
                X1=0
                Y1=1
                X2=5
                Y2=6

            if tipo == 1 and cuantos == 4 :
                X1=1
                Y1=1
                X2=10
                Y2=6

            plt.xlim([X1-2, X2+10])
            plt.ylim([Y1-2, Y2+4])

            dx = abs(X2 - X1)
            dy = abs(Y2 - Y1)
            steps = 0

            if (dx) > (dy):
                steps = (dx)
            else:
                steps = (dy)

            xInc = float(dx / steps)
            yInc = float(dy / steps)

            xInc = round(xInc,1)
            yInc = round(yInc,1)

            x_g = X1
            y_g = Y1

            if cuantos == 1:

                print('Cuadrado DDA\n')
                print('X   Y\n')

                for i in range(0, int(steps)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    x_g += xInc
                    y_g += yInc
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                for i in range(0, int(steps)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    x_g += 1
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                for i in range(0, int(steps)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    y_g -= yInc
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                for i in range(0, int(steps)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    x_g -= 1
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                plt.show()
                print('\n')

            if cuantos == 2:

                print('Rectangulo DDA\n')
                print('X   Y\n')

                for i in range(0, int(steps)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    x_g += xInc
                    y_g += yInc
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                for i in range(0, int(steps + 3)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    x_g += 1
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                for i in range(0, int(steps)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    y_g -= yInc
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                for i in range(0, int(steps + 3)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    x_g -= 1
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                plt.show()
                print('\n')

            if cuantos == 3:

                print('Triangulo DDA\n')
                print('X   Y\n')

                for i in range(0, int(steps)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    x_g += xInc
                    y_g += yInc
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                for i in range(0, int(steps)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    y_g -= 1
                    x_g += 1
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                for i in range(0, int(steps+5)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    x_g -= 1
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                plt.show()
                print('\n')

            if cuantos == 4:

                print('Triangulo Recatangulo DDA\n')
                print('X   Y\n')

                for i in range(0, int(steps)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    x_g += xInc
                    y_g += yInc
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                for i in range(0, int(steps)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    y_g -= yInc
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                for i in range(0, int(steps+1)):
                    g1= matplotlib.patches.Rectangle((round(x_g), round(y_g)),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f1.add_patch(g1)
                    x_g -= 1
                    x_r = round(x_g)
                    y_r = round(y_g)
                    print(str(x_r) + "   " + str(y_r)+ '\n')

                plt.show()
                print('\n')




# OPCION BRESENHAMS
    if tipo == 2:
        print("BRESENHAMS")
        cuantos = int(input("Selecciona uno\n1.Cuadrado\n2.Rectangulo\n3.Triangulo \n4.triangulo rectangulo\nCon que figura quieres trabajar: "))

        if tipo == 2:
            f2 = plt.figure(2).add_subplot(1,1,1)
            plt.title("Algoritmo Bresenhams")
            plt.grid()

            if tipo == 2 and cuantos == 1 or cuantos == 2:
                X1=4
                Y1=2
                X2=8
                Y2=2

            if tipo == 2 and cuantos == 3 :
                X1=0
                Y1=1
                X2=5
                Y2=6

            if tipo == 2 and cuantos == 4 :
                X1=1
                Y1=1
                X2=10
                Y2=6

            plt.xlim([X1-2, X2+12])
            plt.ylim([Y1-2, Y2+12])

            dx = abs(X2 - X1)
            dy = abs(Y2 - Y1)
            p = 2*dy - dx

            X = X1
            Y = Y1

            if cuantos == 1:

                print('Cuadrado Bresenhams\n')
                print('X   Y\n')

                while (X <= X2):
                    print(str(X) + "   " + str(Y)+ '\n')
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    if(dx < 0):
                        X-=1
                    else:
                        X+=1

                    if (dy <0):
                        if p < 0:
                            p = p + 2 * dy
                            Y-=1
                        else:
                            p = p + (2*dy) -(2*dx)
                    else:
                        if(p < 0):
                            p = p + 2 * dy
                        else:
                            p = p + (2*dy) -(2*dx)
                            Y+=1

                for i in range(Y+1, X2):
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    Y+=1
                    print(str(X) + "   " + str(Y)+'\n')

                for i in range(X2-X1, X):
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    X-=1
                    print(str(X) + "   " + str(Y)+'\n')

                for i in range(Y-Y+2, X2):
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    Y-=1
                    print(str(X) + "   " + str(Y)+'\n')

                plt.show()
                print('\n')

            if cuantos == 2:

                print('Rectangulo Bresenhams\n')
                print('X   Y\n')

                while (X <= X2):
                    print(str(X) + "   " + str(Y)+ '\n')
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    if(dx < 0):
                        X-=1
                    else:
                        X+=1

                    if (dy <0):
                        if p < 0:
                            p = p + 2 * dy
                            Y-=1
                        else:
                            p = p + (2*dy) -(2*dx)
                    else:
                        if(p < 0):
                            p = p + 2 * dy
                        else:
                            p = p + (2*dy) -(2*dx)
                            Y+=1

                for i in range(Y+1, X2+5):
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)     
                    Y+=1
                    print(str(X) + "   " + str(Y)+'\n')

                for i in range(X2-X1, X):
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    X-=1
                    print(str(X) + "   " + str(Y)+'\n')

                for i in range(Y-Y+2, X2+5):
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    Y-=1
                    print(str(X) + "   " + str(Y)+'\n')

                plt.show()
                print('\n')

            if cuantos == 3:

                print('Triangulo Bresenhams\n')
                print('X   Y\n')

                while (X <= X2):
                    print(str(X) + "   " + str(Y)+ '\n')
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    if(dx < 0):
                        X-=1
                    else:
                        X+=1

                    if (dy <0):
                        if p < 0:
                            p = p + 2 * dy
                            Y-=1
                        else:
                            p = p + (2*dy) -(2*dx)
                    else:
                        if(p < 0):
                            p = p + 2 * dy
                        else:
                            p = p + (2*dy) -(2*dx)
                            Y+=1

                for i in range(X, X2+8):
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    X += 1
                    Y -= 1
                    print(str(X) + "   " + str(Y)+ '\n')

                for i in range(X, X2+23):
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    X -= 1
                    print(str(X) + "   " + str(Y)+ '\n')

                plt.show()
                print('\n')

            if cuantos == 4:

                print('Triangulo Rectangulo Bresenhams\n')
                print('X   Y\n')

                while (X <= X2):
                    print(str(X) + "   " + str(Y)+ '\n')
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    if(dx < 0):
                        X-=1
                    else:
                        X+=1

                    if (dy <0):
                        if p < 0:
                            p = p + 2 * dy
                            Y-=1
                        else:
                            p = p + (2*dy) -(2*dx)
                    else:
                        if(p < 0):
                            p = p + 2 * dy
                        else:
                            p = p + (2*dy) -(2*dx)
                            Y+=1

                for i in range(X, X2+7):
                    g2= matplotlib.patches.Rectangle((X, Y-1),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    Y -= 1

                    print(str(X) + "   " + str(Y)+ '\n')

                for i in range(X, X2+12):
                    g2= matplotlib.patches.Rectangle((X, Y),1,1,linewidth=2,edgecolor='b', facecolor='none')
                    f2.add_patch(g2)
                    X -= 1
                    print(str(X) + "   " + str(Y)+ '\n')

                plt.show()
                print('\n')

if __name__ == "__main__":
    main()
