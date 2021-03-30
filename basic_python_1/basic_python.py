import numpy as np 
import matplotlib.pyplot as plt

class BasicPythonBasic1:
    def __init__(self):
        set_amplitude = float(input('Input amplitube: '))
        set_frequency = float(input('Input frequency: '))
        self.save_setting(set_amplitude, set_frequency)
        sample_time = np.linspace(0, 2*np.pi, 1000)
        sin_result = set_amplitude*np.sin(set_frequency*sample_time
        cos_result = set_amplitude*np.cos(set_frequency*sample_time)
        tan_result = set_amplitude*np.tan(set_frequency*sample_time)
        self.draw_result(sin_result, cos_result, tan_result, sample_time)
    
    def draw_result(self, sin_result, cos_result, tan_result, sample_time):        
        fig, [[sin_fig, cos_fig],[tan_fig, null_fig]] = \
                plt.subplots(ncols=2, nrows=2, sharex=False, sharey=False,\
                figsize=(10,20),gridspec_kw={'height_ratios': [1, 2]})

        sin_fig.plot(sample_time, sin_result)
        sin_fig.set_title('sin')
        sin_fig.set_xlim(0, 2*np.pi)
        sin_fig.set_ylabel('amplitude')
        sin_fig.grid(True)

        cos_fig.plot(sample_time, cos_result)
        cos_fig.set_title('cos')
        cos_fig.set_xlim(0, 2*np.pi)
        cos_fig.grid(True)

        tan_fig.plot(sample_time, tan_result)
        tan_fig.set_title('tan')
        tan_fig.set_xlim(0, 2*np.pi)
        tan_fig.set_xlabel('sample_time')
        tan_fig.set_ylabel('amplitude')
        tan_fig.grid(True)

        fig.show()
        try:
            plt.pause(0)
        except:
            pass
    
    def save_setting(self, set_amplitude, set_frequency):
        with open("save_result.txt", "w") as text_file:
            save_inf = "set_amplitude: "+str(set_amplitude) + ", set_frequency: "+str(set_frequency)
            print(save_inf, file=text_file)

if __name__ == '__main__':
    try:
        BasicPythonBasic1()
    except KeyboardInterrupt:
        print("Shutting down")