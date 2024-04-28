from tkinter import *
from tkinter import ttk


WIDTH = 400
HEIGHT = 350
TITLE = "Расчет энергопотребления"
IS_RESIZABLE_X = False
IS_RESIZABLE_Y = False


def build_elements():
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[10, 10])

    power = IntVar()
    operating_time = IntVar()
    energy_cost = DoubleVar()

    label1 = Label(frame, text="Нагрузка, Вт")
    label2 = Label(frame, text="Время работы, часы")
    label3 = Label(frame, text="Тариф за 1 кВт-ч.")

    entry1 = ttk.Entry(frame, textvariable=power, width=15)
    entry2 = ttk.Entry(frame, textvariable=operating_time, width=15)
    entry3 = ttk.Entry(frame, textvariable=energy_cost, width=15)

    label1.grid(row=0, column=0, padx=20, pady=5)
    label2.grid(row=1, column=0, padx=20, pady=5)
    label3.grid(row=2, column=0, padx=20, pady=5)

    entry1.grid(row=0, column=1, padx=20, pady=5,)
    entry2.grid(row=1, column=1, padx=20, pady=5,)
    entry3.grid(row=2, column=1, padx=20, pady=5,)
    return frame, entry1, entry2, entry3


def build_buttons(*args):
    frame = ttk.Frame(borderwidth=1,  padding=[5, 5])
    btn_count = ttk.Button(frame, text="Рассчитать", command=args[0], width=15)
    btn_clear = ttk.Button(frame, text="Очистить", command=args[1], width=15)
    btn_count.grid(row=0, column=0, padx=10, pady=5, )
    btn_clear.grid(row=0, column=1, padx=10, pady=5, )
    return frame, btn_count, btn_clear


def calculate_energy():
    try:
        power = int(input_entry1.get()) / 1000
        operating_time = int(input_entry2.get())
        energy_cost = float(input_entry3.get())
    except ValueError:
        result_consumption.set("ОШИБКА: Неправильный формат входных данных")
    else:
        consumption = power * operating_time
        total_cost = consumption * energy_cost
        result_consumption.set(f"Энергопотребление: {round(consumption, 4)} кВт × ч")
        result_total_cost.set(f"Стоимость потребленной энергии: {round(total_cost, 4)} рублей за кВт × ч")


def clear_entries():
    input_entry1.delete(0, 'end')
    input_entry2.delete(0, 'end')
    input_entry3.delete(0, 'end')
    result_consumption.set("0")
    result_total_cost.set("0")


root = Tk()
root.title(TITLE)
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(IS_RESIZABLE_X, IS_RESIZABLE_Y)

label = Label(text="Введите ваши данные")
label.pack(anchor=CENTER, pady=10)

result_consumption = StringVar(value="")
result_total_cost = StringVar(value="")

res_label_consumption = Label(textvariable=result_consumption, text="")
res_label_cost = Label(textvariable=result_total_cost, text="")

input_frame, input_entry1, input_entry2, input_entry3 = build_elements()
input_frame.pack(anchor=CENTER, padx=10, pady=10)

frame_btns, btn1, btn2 = build_buttons(calculate_energy, clear_entries)
frame_btns.pack(anchor=CENTER, padx=10, pady=10)

res_label_consumption.pack(anchor=NW, padx=30, pady=5)
res_label_cost.pack(anchor=NW, padx=30, pady=5)


def main():
    root.mainloop()


if __name__ == '__main__':
    main()
