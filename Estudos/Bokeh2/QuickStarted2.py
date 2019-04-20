from bokeh.plotting import figure, output_file, show

# prepare some data
x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y0 = [i**2 for i in x]
y1 = [10**i for i in x]
y2 = [10**(i**2) for i in x]

#Arquivo de saida
output_file('log_lines.html')

#Criando um plot
p = figure(
    tools="pan,box_zoom,reset,save",
    y_axis_type="log",
    y_range=[0.001,10**11],
    title='Saida',
    x_axis_label='secção',
    y_axis_label='particulas'
)

#add alguns render
p.line(x,x,legend='y=x')
p.circle(x,x,legend='y=x',fill_color='white',size=8)
p.line(x,y0,legend='y=x^2',line_width=3)
p.line(x,y1,legend='y=10^x',line_color='red')
p.circle(x,y1,legend='y=10^x',fill_color='red',size=6,line_color='red')
p.line(x,y2,legend='y=10^x^2',line_color='orange',line_dash='4 4')

#mostrar
show(p)