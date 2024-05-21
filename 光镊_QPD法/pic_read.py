import numpy as np
import matplotlib.pyplot as plt
import data_read as dr


if __name__=='__main__':
    # y1,y2=dr.read_tri()
    y1,y2=dr.read_single()
    x=dr.imp_t()
    fig, ax1 = plt.subplots()
    ax1.plot(x, y1, 'b-', label='move of x')
    ax1.set_xlabel('t/s')
    ax1.set_ylabel(r'x_move/$\mu$m', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2 = ax1.twinx()
    ax2.plot(x, y2, 'r-', label='value of QPD')
    ax2.set_ylabel('QPD', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
    plt.title('phase of QPD')
    plt.show()