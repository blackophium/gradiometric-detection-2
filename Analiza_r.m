%clear all;
close all;

%file = C:\Users\agnie\Desktop\Magisterka\Oprogramowanie
y = csvread('pomiar.csv');
y = y';


%czestotliwosc probkowania:
fs = 392;

%liczba probek:
N = length(y);

%FFT:
ys = y - mean(y);
yf = fft(ys);
F = 0:fs/(N-1):fs;
F = F';
Y(1,1) = 0;
figure();
a = plot(F-fs/2,fftshift(abs(yf)));
xlabel('Czêstotliwoœæ [Hz]');
title('Sygnal po FFT w dz.czêstotliwoœci');
hold on
saveas(a,'1.bmp');

%filtracja:
filtr = zeros(1,N);
filtr(7:33) = 1;
filtr(3967:3993) = 1;
fyy = filtr.*yf;

%odwrotna fft
yy = ifft(fyy);
n2 = length(fyy);
td = 1/fs;
tim = 0:td:(n2-1)*td;
figure()
b = plot(tim,real(yy));
xlabel('Czas [s]');
title('Sygnal po filtracji w dz.czasu');
hold on
saveas(b,'2.bmp');

%przed filtracj¹ w dz. czasu
yy2 = ifft(yf);
n2 = length(yf);
td = 1/fs;
tim = 0:td:(n2-1)*td;
figure()
c = plot(tim,real(yy2));
xlabel('Czas [s]');
title('Sygnal przed filtracja w dz.czasu');
hold on
saveas(c,'3.bmp');