from tkinter import*
import time
from colorsys import *
from tkinter import ttk
import random

root=Tk()
root.minsize(height=600,width=900)
root.title("Sorting Visualizer")
icon=PhotoImage(file="C:\\Users\\kanti\\Downloads\\sorting.png")
label=ttk.Label(root,image=icon,background="black")
PhotoImage(file='C:\\Users\\kanti\\Downloads\\sorting.png')
label.pack()

def tab1():
    def tab2():
        root.destroy()
        DARK_GRAY = '#65696B'
        LIGHT_GRAY = '#C4C5BF'
        BLUE = '#0CA8F6'
        DARK_BLUE = '#4204CC'
        WHITE = '#FFFFFF'
        BLACK = '#000000'
        RED = '#F22810'
        YELLOW = '#F7E806'
        PINK = '#F50BED'
        LIGHT_GREEN = '#05F50E'
        PURPLE = '#BF01FB'

        def bubble_sort(data, drawData, timeTick):
            size = len(data)
            for i in range(size-1):
                for j in range(size-i-1):
                    if data[j] > data[j+1]:
                        data[j], data[j+1] = data[j+1], data[j]
                        drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )
                        time.sleep(timeTick)                
            drawData(data, [BLUE for x in range(len(data))])
            
        def merge(data, start, mid, end, drawData, timeTick):
            p = start
            q = mid + 1
            tempArray = []
            for i in range(start, end+1):
                if p > mid:
                    tempArray.append(data[q])
                    q+=1
                elif q > end:
                    tempArray.append(data[p])
                    p+=1
                elif data[p] < data[q]:
                    tempArray.append(data[p])
                    p+=1
                else:
                    tempArray.append(data[q])
                    q+=1
            for p in range(len(tempArray)):
                data[start] = tempArray[p]
                start += 1

        def merge_sort(data, start, end, drawData, timeTick):
            if start < end:
                mid = int((start + end) / 2)
                merge_sort(data, start, mid, drawData, timeTick)
                merge_sort(data, mid+1, end, drawData, timeTick)
                merge(data, start, mid, end, drawData, timeTick)
                drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                                else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
                time.sleep(timeTick)
            drawData(data, [BLUE for x in range(len(data))])

        # def counting_sort(data, drawData, timeTick):
        #     n = max(data) + 1
        #     count = [0] * n
        #     for item in data:
        #         count[item] += 1    
        #     k = 0
        #     for i in range(n):
        #         for j in range(count[i]):
        #             data[k] = i
        #             drawData(data, [BLUE for x in range(len(data))] )
        #             time.sleep(timeTick)
        #             k += 1
        #     drawData(data, [BLUE for x in range(len(data))])

        def heapify(data, n, i, drawData, timeTick):
            largest = i
            left = 2*i+1
            right = 2*i+2
            if left < n and data[i] < data[left]:
                largest = left
            if right < n and data[largest] < data[right]:
                largest = right
            if largest != i:
                data[i], data[largest] = data[largest], data[i]
                heapify(data, n, largest, drawData, timeTick)

        def heap_sort(data, drawData, timeTick):
            n = len(data)
            for i in range(n-1, -1, -1):
                heapify(data, n, i, drawData, timeTick)
            for i in range(n-1, 0, -1):
                data[i], data[0] = data[0], data[i]
                heapify(data, i, 0, drawData, timeTick)
                drawData(data, [YELLOW if x == i else BLUE for x in range(n)])
                time.sleep(timeTick)
            drawData(data, [BLUE for x in range(len(data))])

        def insertion_sort(data, drawData, timeTick):
            for i in range(len(data)):
                temp = data[i]
                k = i
                while k > 0 and temp < data[k-1]:
                    data[k] = data[k-1]
                    k -= 1
                data[k] = temp
                drawData(data, [YELLOW if x == k or x == i else BLUE for x in range(len(data))])
                time.sleep(timeTick)        
            drawData(data, [BLUE for x in range(len(data))])

        def partition(data, start, end, drawData, timeTick):
            i = start + 1
            pivot = data[start]
            for j in range(start+1, end+1):
                if data[j] < pivot:
                    data[i], data[j] = data[j], data[i]
                    i+=1
            data[start], data[i-1] = data[i-1], data[start]
            return i-1

        def quick_sort(data, start, end, drawData, timeTick):
            if start < end:
                pivot_position = partition(data, start, end, drawData, timeTick)
                quick_sort(data, start, pivot_position-1, drawData, timeTick)
                quick_sort(data, pivot_position+1, end, drawData, timeTick)
                drawData(data, [PURPLE if x >= start and x < pivot_position else YELLOW if x == pivot_position
                                else DARK_BLUE if x > pivot_position and x <=end else BLUE for x in range(len(data))])
                time.sleep(timeTick)        
            drawData(data, [BLUE for x in range(len(data))])

        def selection_sort(data, drawData, timeTick):
            for i in range(len(data)-1):
                minimum = i
                for k in range(i+1, len(data)):
                    if data[k] < data[minimum]:
                        minimum = k
                data[minimum], data[i] = data[i], data[minimum]
                drawData(data, [YELLOW if x == minimum or x == i else BLUE for x in range(len(data))] )
                time.sleep(timeTick)       
            drawData(data, [BLUE for x in range(len(data))])
            
        window = Tk()
        window.title("Sorting Visualizer")
        window.maxsize(1000, 900)
        window.config(bg = LIGHT_GREEN)
        algorithm_name = StringVar()
        algo_list = ['Bubble Sort','Insertion Sort','Selection Sort','Quick Sort','Merge Sort','Heap Sort']

        speed_name = StringVar()
        speed_list = ['Fast', 'Medium', 'Slow']
        data = []

        def drawData(data, colorArray):
            canvas.delete("all")
            canvas_width = 800
            canvas_height = 400
            x_width = canvas_width / (len(data) + 1)
            offset = 4
            spacing = 2
            normalizedData = [i / max(data) for i in data]

            for i, height in enumerate(normalizedData):
                x0 = i * x_width + offset + spacing
                y0 = canvas_height - height * 390
                x1 = (i + 1) * x_width + offset
                y1 = canvas_height
                canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

            window.update_idletasks()

        def generate():
            global data
            data = []
            for i in range(0, 20):
                random_value = random.randint(1, 15)
                data.append(random_value)
            drawData(data, [BLUE for x in range(len(data))])

        def set_speed():
            if speed_menu.get() == 'Slow':
                return 0.3
            elif speed_menu.get() == 'Medium':
                return 0.1
            else:
                return 0.001

        def sort():
            global data
            timeTick = set_speed()
            
            if algo_menu.get() == 'Bubble Sort':
                bubble_sort(data, drawData, timeTick)
            elif algo_menu.get() == 'Merge Sort':
                merge_sort(data, 0, len(data)-1, drawData, timeTick)
            elif algo_menu.get() == 'Insertion Sort':
                insertion_sort(data,drawData,timeTick)
            elif algo_menu.get() == 'Quick Sort':
                quick_sort(data, 0, len(data)-1, drawData, timeTick)
            elif algo_menu.get() == 'Selection Sort':
                selection_sort(data,drawData,timeTick)
            elif algo_menu.get() == 'Heap Sort':
                heap_sort(data,drawData,timeTick)
        
        UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
        UI_frame.grid(row=0, column=0, padx=10, pady=5)

        l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
        l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
        algo_menu.grid(row=0, column=1, padx=5, pady=5)
        algo_menu.current(0)

        l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
        l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
        speed_menu.grid(row=1, column=1, padx=5, pady=5)
        speed_menu.current(0)
        
        b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
        b1.grid(row=2, column=1, padx=5, pady=5)

        b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
        b3.grid(row=2, column=0, padx=5, pady=5)

        canvas = Canvas(window, width=800, height=400, bg=WHITE)
        canvas.grid(row=1, column=0, padx=10, pady=5)

        window.mainloop()
    # label1=Label(root,text='\n Welcome to the sorting visualizer \n',font=('Times_New_Romen',40))
    label2=Label(root,text='\n Made by Kanti Kumar',font=('Times_New_Romen bold',30),fg="blue")
    label2.pack()

    button1=Button(root,text='NEXT',font=('Times_New_Romen',25),command=tab2,bg="dark gray")
    button1.pack(side=BOTTOM)

tab1()
root.mainloop()