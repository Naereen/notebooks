
% Some variables
N = 100
disp(['Number of values N =', num2str(N)])
h = 1 / N
disp(['Step h = ', num2str(h)])

% Some arrays
t = 0 : h : 2*pi;
x = cos(t);
y = sin(t);
length(t)
length(x)
length(y)

fig = figure();
plot(t, x, 'r*-')
grid on
hold on
plot(t, y, 'b+-')
legend(['\cos(t)', '\sin(t)'])
title('Cosinus and sinus on [0, 2 \pi]')
% whitebg(fig);

fig = figure();
grid on
plot(x, y)
title('\sin(t) as function of \cos(t)')
% whitebg(fig);

a = [[1 0 1]; [0 1 1]; [1 1 0]]

a'

b = 1 + a^5

l_a = eig(a)
l_b = eig(b)

[Ua, Sa, Va] = svd(a)
[Ub, Sb, Vb] = svd(b)

x = linspace(-2, 2, 50);
y = linspace(-2, 2, 50);
[xx,yy] = meshgrid(x, y);
mesh(xx, yy, 4 - (xx.^2 + yy.^2))

x = linspace(-2, 2, 50);
y = linspace(-2, 2, 50);
[xx,yy] = meshgrid(x, y);
meshc(xx, yy, 4 - (xx.^2 + yy.^2))

# From https://octave.sourceforge.io/octave/function/plot3.html
z = [0:0.05:5];
plot3(cos (2*pi*z), sin (2*pi*z), z, ";helix;");
plot3(z, exp (2i*pi*z), ";complex sinusoid;");

clf;
z = [0:0.05:5];
plot3 (cos (2*pi*z), sin (2*pi*z), z);
legend ("helix");
title ("plot3() of a helix");

clf;
colormap ("default");
[X, Y] = meshgrid (linspace (-3, 3, 40));
Z = sqrt (abs (X .* Y)) ./ (1 + X.^2 + Y.^2);
meshc (X, Y, Z);
title ("meshc() combines mesh/contour plots");
