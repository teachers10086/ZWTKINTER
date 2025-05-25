import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser, simpledialog, font
from tkinter import ttk
import threading
import time

# ========== 窗口相关 ==========
def 主窗口(宽=800, 高=600, 标题="主窗口"):
    """创建主窗口"""
    win = tk.Tk()
    win.geometry(f"{宽}x{高}")
    win.title(标题)
    return win

def 新窗口(宽=400, 高=300, 标题="新窗口"):
    """创建新窗口"""
    win = tk.Toplevel()
    win.geometry(f"{宽}x{高}")
    win.title(标题)
    return win

def 运行(win):
    win.mainloop()  # 启动Tkinter的事件循环

def 窗口标题(win, 标题):
    """设置窗口标题"""
    win.title(标题)

def 窗口图标(win, 图标路径):
    """设置窗口图标"""
    try:
        win.iconbitmap(图标路径)
    except:
        pass

def 窗口居中(win):
    """窗口居中显示"""
    win.update_idletasks()
    宽 = win.winfo_width()
    高 = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (宽 // 2)
    y = (win.winfo_screenheight() // 2) - (高 // 2)
    win.geometry(f"{宽}x{高}+{x}+{y}")

def 窗口最大化(win):
    """窗口最大化"""
    win.state('zoomed')

def 窗口最小化(win):
    """窗口最小化"""
    win.iconify()

def 窗口置顶(win, 置顶=True):
    """设置窗口置顶"""
    win.attributes('-topmost', 置顶)

def 窗口透明度(win, 透明度=1.0):
    """设置窗口透明度 (0.0-1.0)"""
    win.attributes('-alpha', 透明度)

def 窗口不可调整(win):
    """禁止调整窗口大小"""
    win.resizable(False, False)

def 窗口全屏(win, 全屏=True):
    """设置全屏模式"""
    win.attributes('-fullscreen', 全屏)

def 关闭窗口(win):
    """关闭窗口"""
    win.destroy()

def 隐藏窗口(win):
    """隐藏窗口"""
    win.withdraw()

def 显示窗口(win):
    """显示窗口"""
    win.deiconify()

# ========== 基础控件 ==========
def 标签(win, 内容="", 行=0, 列=0, 跨行=1, 跨列=1, 字体=None, 颜色=None, 背景色=None, 对齐='w'):
    """创建标签"""
    label = tk.Label(win, text=内容, font=字体, fg=颜色, bg=背景色, anchor=对齐)
    label.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='ew')
    return label


def 按钮(win, 文本="按钮", 命令=None, 行=0, 列=0, 跨行=1, 跨列=1, 宽=None, 高=None, 字体=None, 颜色=None, 背景色=None):
    """创建按钮"""
    btn = tk.Button(win, text=文本, command=命令, width=宽, height=高, font=字体, fg=颜色, bg=背景色)
    btn.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5)
    return btn

def 输入框(win, 默认值="", 行=0, 列=0, 跨行=1, 跨列=1, 宽=None, 字体=None, 显示字符=None):
    """创建输入框"""
    entry = tk.Entry(win, width=宽, font=字体, show=显示字符)
    if 默认值:
        entry.insert(0, 默认值)
    entry.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='ew')
    return entry

def 文本框(win, 行=0, 列=0, 跨行=1, 跨列=1, 宽=40, 高=10, 字体=None, 换行=True):
    """创建文本框"""
    wrap = tk.WORD if 换行 else tk.NONE
    text = tk.Text(win, width=宽, height=高, font=字体, wrap=wrap)
    text.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='nsew')
    return text

def 下拉框(win, 选项列表, 默认选择=0, 行=0, 列=0, 跨行=1, 跨列=1):
    """创建下拉框"""
    var = tk.StringVar(win)
    if 选项列表:
        var.set(选项列表[默认选择])
    opt = tk.OptionMenu(win, var, *选项列表)
    opt.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5)
    return var, opt

def 列表框(win, 选项列表=None, 行=0, 列=0, 跨行=1, 跨列=1, 宽=20, 高=10, 多选=False):
    """创建列表框"""
    选择模式 = tk.EXTENDED if 多选 else tk.SINGLE
    listbox = tk.Listbox(win, width=宽, height=高, selectmode=选择模式)
    if 选项列表:
        for 项 in 选项列表:
            listbox.insert(tk.END, 项)
    listbox.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='nsew')
    return listbox

# ========== 选择控件 ==========
def 复选框(win, 文本="", 行=0, 列=0, 跨行=1, 跨列=1, 默认选中=False):
    """创建复选框"""
    var = tk.BooleanVar()
    var.set(默认选中)
    cb = tk.Checkbutton(win, text=文本, variable=var)
    cb.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='w')
    return var, cb

def 单选框(win, 文本="", 值="", 变量=None, 行=0, 列=0, 跨行=1, 跨列=1):
    """创建单选框"""
    if 变量 is None:
        变量 = tk.StringVar()
    rb = tk.Radiobutton(win, text=文本, variable=变量, value=值)
    rb.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='w')
    return 变量, rb

def 单选框组(win, 选项列表, 默认选择=0, 行=0, 列=0, 方向='vertical'):
    """创建单选框组"""
    var = tk.StringVar()
    if 选项列表:
        var.set(选项列表[默认选择])
    
    按钮组 = []
    for i, 选项 in enumerate(选项列表):
        if 方向 == 'vertical':
            当前行, 当前列 = 行 + i, 列
        else:
            当前行, 当前列 = 行, 列 + i
        
        rb = tk.Radiobutton(win, text=选项, variable=var, value=选项)
        rb.grid(row=当前行, column=当前列, padx=5, pady=2, sticky='w')
        按钮组.append(rb)
    
    return var, 按钮组

# ========== 滑块和进度条 ==========
def 滑块(win, 最小值=0, 最大值=100, 默认值=0, 方向='horizontal', 行=0, 列=0, 跨行=1, 跨列=1, 长度=200):
    """创建滑块"""
    orient = tk.HORIZONTAL if 方向 == 'horizontal' else tk.VERTICAL
    scale = tk.Scale(win, from_=最小值, to=最大值, orient=orient, length=长度)
    scale.set(默认值)
    scale.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5)
    return scale

def 进度条(win, 最大值=100, 行=0, 列=0, 跨行=1, 跨列=1, 长度=200, 模式='determinate'):
    """创建进度条"""
    style = ttk.Style()
    pb = ttk.Progressbar(win, maximum=最大值, length=长度, mode=模式)
    pb.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5)
    return pb

def 旋转框(win, 最小值=0, 最大值=100, 默认值=0, 步长=1, 行=0, 列=0, 跨行=1, 跨列=1, 宽=10):
    """创建数字旋转框"""
    spinbox = tk.Spinbox(win, from_=最小值, to=最大值, value=默认值, increment=步长, width=宽)
    spinbox.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5)
    return spinbox

# ========== 框架和容器 ==========
def 框架(win, 行=0, 列=0, 跨行=1, 跨列=1, 边框类型='flat', 边框宽度=1, 背景色=None):
    """创建框架"""
    frame = tk.Frame(win, relief=边框类型, bd=边框宽度, bg=背景色)
    frame.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='nsew')
    return frame

def 标签框架(win, 标题="", 行=0, 列=0, 跨行=1, 跨列=1):
    """创建带标签的框架"""
    lf = tk.LabelFrame(win, text=标题)
    lf.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='nsew')
    return lf

def 分页控件(win, 行=0, 列=0, 跨行=1, 跨列=1):
    """创建分页控件"""
    notebook = ttk.Notebook(win)
    notebook.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='nsew')
    return notebook

def 添加页面(notebook, 标题, 内容=None):
    """为分页控件添加页面"""
    if 内容 is None:
        内容 = tk.Frame(notebook)
    notebook.add(内容, text=标题)
    return 内容

def 分隔器(win, 方向='horizontal', 行=0, 列=0, 跨行=1, 跨列=1):
    """创建分隔器"""
    orient = tk.HORIZONTAL if 方向 == 'horizontal' else tk.VERTICAL
    separator = ttk.Separator(win, orient=orient)
    separator.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='ew')
    return separator

# ========== 滚动条 ==========
def 滚动条(win, 方向='vertical', 行=0, 列=0, 跨行=1, 跨列=1):
    """创建滚动条"""
    orient = tk.VERTICAL if 方向 == 'vertical' else tk.HORIZONTAL
    scrollbar = tk.Scrollbar(win, orient=orient)
    scrollbar.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, sticky='ns' if 方向 == 'vertical' else 'ew')
    return scrollbar

def 带滚动条的文本框(win, 行=0, 列=0, 跨行=1, 跨列=1, 宽=40, 高=10):
    """创建带滚动条的文本框"""
    frame = tk.Frame(win)
    frame.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='nsew')
    
    text = tk.Text(frame, width=宽, height=高, wrap=tk.WORD)
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)
    
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    return text, scrollbar

def 带滚动条的列表框(win, 选项列表=None, 行=0, 列=0, 跨行=1, 跨列=1, 宽=20, 高=10):
    """创建带滚动条的列表框"""
    frame = tk.Frame(win)
    frame.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='nsew')
    
    listbox = tk.Listbox(frame, width=宽, height=高)
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
    listbox.configure(yscrollcommand=scrollbar.set)
    
    if 选项列表:
        for 项 in 选项列表:
            listbox.insert(tk.END, 项)
    
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    return listbox, scrollbar

# ========== 高级控件 ==========
def 树形控件(win, 列名列表=None, 行=0, 列=0, 跨行=1, 跨列=1, 高=10):
    """创建树形控件"""
    if 列名列表 is None:
        列名列表 = ['名称']
    
    tree = ttk.Treeview(win, columns=列名列表[1:], height=高)
    tree.heading('#0', text=列名列表[0])
    
    for i, 列名 in enumerate(列名列表[1:], 1):
        tree.heading(f'#{i}', text=列名)
        tree.column(f'#{i}', width=100)
    
    tree.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='nsew')
    return tree

def 表格(win, 列名列表, 数据=None, 行=0, 列=0, 跨行=1, 跨列=1, 高=10):
    """创建表格"""
    tree = ttk.Treeview(win, columns=列名列表, show='headings', height=高)
    
    for 列名 in 列名列表:
        tree.heading(列名, text=列名)
        tree.column(列名, width=100)
    
    if 数据:
        for 行数据 in 数据:
            tree.insert('', tk.END, values=行数据)
    
    tree.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5, sticky='nsew')
    return tree

def 日历控件(win, 行=0, 列=0, 跨行=1, 跨列=1):
    """创建日历控件（需要安装tkcalendar）"""
    try:
        from tkcalendar import Calendar
        cal = Calendar(win)
        cal.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5)
        return cal
    except ImportError:
        标签(win, "需要安装tkcalendar库", 行, 列, 跨行, 跨列)
        return None

# ========== 对话框 ==========
def 弹窗(标题, 内容):
    """信息弹窗"""
    messagebox.showinfo(标题, 内容)

def 警告弹窗(标题, 内容):
    """警告弹窗"""
    messagebox.showwarning(标题, 内容)

def 错误弹窗(标题, 内容):
    """错误弹窗"""
    messagebox.showerror(标题, 内容)

def 确认弹窗(标题, 内容):
    """确认弹窗"""
    return messagebox.askyesno(标题, 内容)

def 询问弹窗(标题, 内容):
    """询问弹窗（是/否/取消）"""
    return messagebox.askyesnocancel(标题, 内容)

def 输入对话框(标题, 提示="请输入:", 默认值=""):
    """输入对话框"""
    return simpledialog.askstring(标题, 提示, initialvalue=默认值)

def 整数输入对话框(标题, 提示="请输入整数:", 默认值=0, 最小值=None, 最大值=None):
    """整数输入对话框"""
    return simpledialog.askinteger(标题, 提示, initialvalue=默认值, minvalue=最小值, maxvalue=最大值)

def 浮点数输入对话框(标题, 提示="请输入数字:", 默认值=0.0, 最小值=None, 最大值=None):
    """浮点数输入对话框"""
    return simpledialog.askfloat(标题, 提示, initialvalue=默认值, minvalue=最小值, maxvalue=最大值)

def 选择文件():
    """选择单个文件"""
    return filedialog.askopenfilename()

def 选择多个文件():
    """选择多个文件"""
    return filedialog.askopenfilenames()

def 选择文件夹():
    """选择文件夹"""
    return filedialog.askdirectory()

def 保存文件():
    """保存文件对话框"""
    return filedialog.asksaveasfilename()

def 选择颜色():
    """颜色选择器"""
    color = colorchooser.askcolor()
    return color[1] if color[1] else None

# ========== 菜单相关 ==========
def 菜单栏(win, 菜单结构):
    """创建菜单栏"""
    menubar = tk.Menu(win)
    for 菜单名称, 子菜单 in 菜单结构.items():
        子菜单栏 = tk.Menu(menubar, tearoff=0)
        for 项名, 命令 in 子菜单.items():
            if 项名 == "分隔线":
                子菜单栏.add_separator()
            else:
                子菜单栏.add_command(label=项名, command=命令)
        menubar.add_cascade(label=菜单名称, menu=子菜单栏)
    win.config(menu=menubar)
    return menubar

def 右键菜单(win, 菜单结构):
    """创建右键菜单"""
    menu = tk.Menu(win, tearoff=0)
    for 项名, 命令 in 菜单结构.items():
        if 项名 == "分隔线":
            menu.add_separator()
        else:
            menu.add_command(label=项名, command=命令)
    
    def 显示菜单(event):
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()
    
    win.bind("<Button-3>", 显示菜单)
    return menu

def 工具栏(win, 按钮列表, 行=0, 列=0):
    """创建工具栏"""
    toolbar = tk.Frame(win)
    toolbar.grid(row=行, column=列, sticky='ew', padx=5, pady=5)
    
    按钮组 = []
    for i, (文本, 命令) in enumerate(按钮列表):
        btn = tk.Button(toolbar, text=文本, command=命令)
        btn.pack(side=tk.LEFT, padx=2)
        按钮组.append(btn)
    
    return toolbar, 按钮组

def 状态栏(win, 默认文本="就绪"):
    """创建状态栏"""
    status_frame = tk.Frame(win)
    status_frame.grid(row=999, column=0, columnspan=999, sticky='ew')
    
    status_label = tk.Label(status_frame, text=默认文本, bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_label.pack(fill=tk.X)
    
    return status_frame, status_label

# ========== 布局管理 ==========
def 自动布局(win, 行数=100, 列数=100):
    """自动调整网格布局权重"""
    for i in range(行数):
        win.rowconfigure(i, weight=1)
    for j in range(列数):
        win.columnconfigure(j, weight=1)

def 设置行权重(win, 行号, 权重=1):
    """设置指定行的权重"""
    win.rowconfigure(行号, weight=权重)

def 设置列权重(win, 列号, 权重=1):
    """设置指定列的权重"""
    win.columnconfigure(列号, weight=权重)

def 清空布局(win):
    """清空窗口所有控件"""
    for widget in win.winfo_children():
        widget.destroy()

# ========== 事件绑定 ==========
def 绑定事件(控件, 事件, 函数):
    """绑定事件到控件"""
    控件.bind(事件, 函数)

def 绑定双击(控件, 函数):
    """绑定双击事件"""
    控件.bind("<Double-Button-1>", 函数)

def 绑定右键(控件, 函数):
    """绑定右键点击事件"""
    控件.bind("<Button-3>", 函数)

def 绑定按键(win, 按键, 函数):
    """绑定按键事件"""
    win.bind(按键, 函数)

def 绑定鼠标进入(控件, 函数):
    """绑定鼠标进入事件"""
    控件.bind("<Enter>", 函数)

def 绑定鼠标离开(控件, 函数):
    """绑定鼠标离开事件"""
    控件.bind("<Leave>", 函数)

# ========== 样式和外观 ==========
def 设置字体(控件, 字体名="Arial", 大小=12, 样式="normal"):
    """设置控件字体"""
    控件.config(font=(字体名, 大小, 样式))

def 设置颜色(控件, 前景色=None, 背景色=None):
    """设置控件颜色"""
    if 前景色:
        控件.config(fg=前景色)
    if 背景色:
        控件.config(bg=背景色)

def 设置边框(控件, 类型='flat', 宽度=1):
    """设置控件边框"""
    控件.config(relief=类型, bd=宽度)

def 设置鼠标样式(控件, 样式='hand2'):
    """设置鼠标指针样式"""
    控件.config(cursor=样式)

def 禁用控件(控件):
    """禁用控件"""
    控件.config(state='disabled')

def 启用控件(控件):
    """启用控件"""
    控件.config(state='normal')

# ========== 图像处理 ==========
def 加载图片(图片路径, 宽度=None, 高度=None):
    """加载图片"""
    try:
        from PIL import Image, ImageTk
        img = Image.open(图片路径)
        if 宽度 and 高度:
            img = img.resize((宽度, 高度), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except ImportError:
        # 如果没有PIL，使用tkinter自带的PhotoImage
        return tk.PhotoImage(file=图片路径)

def 图片标签(win, 图片路径, 行=0, 列=0, 跨行=1, 跨列=1, 宽度=None, 高度=None):
    """创建图片标签"""
    img = 加载图片(图片路径, 宽度, 高度)
    label = tk.Label(win, image=img)
    label.image = img  # 保持引用
    label.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5)
    return label

def 图片按钮(win, 图片路径, 命令=None, 行=0, 列=0, 跨行=1, 跨列=1, 宽度=None, 高度=None):
    """创建图片按钮"""
    img = 加载图片(图片路径, 宽度, 高度)
    btn = tk.Button(win, image=img, command=命令)
    btn.image = img  # 保持引用
    btn.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5)
    return btn

# ========== 画布控件 ==========
def 画布(win, 宽=400, 高=300, 背景色='white', 行=0, 列=0, 跨行=1, 跨列=1):
    """创建画布"""
    canvas = tk.Canvas(win, width=宽, height=高, bg=背景色)
    canvas.grid(row=行, column=列, rowspan=跨行, columnspan=跨列, padx=5, pady=5)
    return canvas

def 画线(画布, x1, y1, x2, y2, 颜色='black', 宽度=1):
    """在画布上画线"""
    return 画布.create_line(x1, y1, x2, y2, fill=颜色, width=宽度)

def 画矩形(画布, x1, y1, x2, y2, 边框色='black', 填充色=None, 线宽=1):
    """在画布上画矩形"""
    return 画布.create_rectangle(x1, y1, x2, y2, outline=边框色, fill=填充色, width=线宽)

def 画圆(画布, x1, y1, x2, y2, 边框色='black', 填充色=None, 线宽=1):
    """在画布上画圆"""
    return 画布.create_oval(x1, y1, x2, y2, outline=边框色, fill=填充色, width=线宽)

def 画文字(画布, x, y, 文字, 字体=None, 颜色='black'):
    """在画布上写文字"""
    return 画布.create_text(x, y, text=文字, font=字体, fill=颜色)

def 清空画布(画布):
    """清空画布"""
    画布.delete("all")


# ========== 定时器和线程 ==========
def 定时器(win, 间隔, 函数, 重复=True):
    """创建定时器"""

    def 执行():
        函数()  # 执行传入的函数
        if 重复:
            # 如果重复，使用 win.after 重新调用执行函数
            win.after(间隔, 执行)

    # 启动定时器，间隔时间后执行一次
    win.after(间隔, 执行)
