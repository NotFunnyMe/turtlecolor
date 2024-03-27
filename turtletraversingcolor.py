import turtle
import random as r

turtle.bgcolor("black")
seurat = turtle.Turtle()

width = 5
height = 7

seurat.penup()
list_color = ["red", "green", "blue", "yellow", "purple","white","orange","cyan","pink","brown","voilet","grey"]


dot_distance = 25
seurat.setpos(-250,250)

def spiralPrint(m,n):
    '''
    m - no of rows
    n - no of columns
    a - matrix
    '''
    k = 0
    l = 0
    f = 0
    seurat.color("white")
    '''
    k - starting row index
    m - ending row index
    '''
    col = r.randint(0,12)
    seurat.color(list_color[col])
    while(k<m and l<n):

        if f==1:
            seurat.right(90)
        # Print the first row from the remaining rows
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            # print(a[k][i],end=" ")
        k+=1
        f=1

        seurat.right(90)
        col = r.randint(0,12)
        seurat.color(list_color[col])

        # Print the last column from the remaining columns
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            # print(a[i][n-1],end=" ")
        n-=1

        seurat.right(90)
        col = r.randint(0,12)
        seurat.color(list_color[col])

        if(k<m):
        # Print the last row from the remaining rows
            for i in range(n-1,l-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                # print(a[m-1][i],end=" ")
            m-=1

            seurat.right(90)
        col = r.randint(0,12)
        seurat.color(list_color[col])
           
        if(l<n):
        # Print the first column from the remaining columns
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                # print(a[i][l],end=" ")
            l+=1

spiralPrint(20,20)

