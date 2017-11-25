
versioninfo()

# If needed:
#Pkg.add("DifferentialEquations")
#Pkg.add("PyPlot")
#Pkg.add("Plots")

using Plots
gr()
using DifferentialEquations

b = 0.25
c = 5.0

y0 = [pi - 0.1; 0.0]

function pend(t, y, dy)
    dy[1] = y[2]
    dy[2] = (-b * y[2]) - (c * sin(y[1]))
end

function f_pend(y, t)
    return [y[2], (-b * y[2]) - (c * sin(y[1]))]
end

tspan = (0.0, 10.0)

function odeint_1(f, y0, tspan)
    prob = ODEProblem(f, y0, tspan)
    sol = solve(prob)
    return sol.t, hcat(sol.u...)'
end

function odeint(f, y0, tspan)
    t, sol = odeint_1(f, y0, tspan)
    return sol
end

t, sol = odeint_1(pend, y0, tspan)

plot(t, sol[:, 1], xaxis="Time t", title="Solution to the pendulum ODE", label="\\theta (t)")
plot!(t, sol[:, 2], label="\\omega (t)")

function rungekutta1(f, y0, t)
    n = length(t)
    y = zeros((n, length(y0)))
    y[1,:] = y0
    for i in 1:n-1
        h = t[i+1] - t[i]
        y[i+1,:] = y[i,:] + h * f(y[i,:], t[i])
    end
    return y
end

t = linspace(0, 10, 101);
sol = rungekutta1(f_pend, y0, t);

plot(t, sol[:, 1], xaxis="Time t", title="Solution to the pendulum ODE with Runge-Kutta 1", label="\\theta (t)")
plot!(t, sol[:, 2], label="\\omega (t)")

t2 = linspace(0, 10, 1001);
sol2 = rungekutta1(f_pend, y0, t2);

plot(t2, sol2[:, 1], xaxis="Time t", title="Solution to the pendulum ODE with Runge-Kutta 1", label="\\theta (t)")
plot!(t2, sol2[:, 2], label="\\omega (t)")

t3 = linspace(0, 10, 2001);
sol3 = rungekutta1(f_pend, y0, t3);

plot(t3, sol3[:, 1], xaxis="Time t", title="Solution to the pendulum ODE with Runge-Kutta 1", label="\\theta (t)")
plot!(t3, sol3[:, 2], label="\\omega (t)")

function rungekutta2(f, y0, t)
    n = length(t)
    y = zeros((n, length(y0)))
    y[1,:] = y0
    for i in 1:n-1
        h = t[i+1] - t[i]
        y[i+1,:] = y[i,:] + h * f(y[i,:] + f(y[i,:], t[i]) * h/2, t[i] + h/2)
    end
    return y
end

t3 = linspace(0, 10, 21);
sol3 = rungekutta2(f_pend, y0, t3);

plot(t3, sol3[:, 1], xaxis="Time t", title="Solution to the pendulum ODE with Runge-Kutta 2 (21 points)", label="\\theta (t)")
plot!(t3, sol3[:, 2], label="\\omega (t)")

t3 = linspace(0, 10, 101);
sol3 = rungekutta2(f_pend, y0, t3);

plot(t3, sol3[:, 1], xaxis="Time t", title="Solution to the pendulum ODE with Runge-Kutta 2 (101 points)", label="\\theta (t)")
plot!(t3, sol3[:, 2], label="\\omega (t)")

function rungekutta4(f, y0, t)
    n = length(t)
    y = zeros((n, length(y0)))
    y[1,:] = y0
    for i in 1:n-1
        h = t[i+1] - t[i]
        k1 = f(y[i,:], t[i])
        k2 = f(y[i,:] + k1 * h/2, t[i] + h/2)
        k3 = f(y[i,:] + k2 * h/2, t[i] + h/2)
        k4 = f(y[i,:] + k3 * h, t[i] + h)
        y[i+1,:] = y[i,:] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    end
    return y
end

t = linspace(0, 10, 31);
sol = rungekutta4(f_pend, y0, t);

plot(t, sol[:, 1], xaxis="Time t", title="Solution to the pendulum ODE with Runge-Kutta 4 (31 points)", label="\\theta (t)")
plot!(t, sol[:, 2], label="\\omega (t)")

t = linspace(0, 10, 101);
sol = rungekutta4(f_pend, y0, t);

plot(t, sol[:, 1], xaxis="Time t", title="Solution to the pendulum ODE with Runge-Kutta 4 (101 points)", label="\\theta (t)")
plot!(t, sol[:, 2], label="\\omega (t)")

methods = [rungekutta1, rungekutta2, rungekutta4]
markers = [:o, :s, :>]

function test_1(n=101)
    t = linspace(0, 10, n)
    tspan = (0.0, 10.0)
    t1, sol = odeint_1(pend, y0, tspan)
    plt = plot(t1, sol[:, 1], marker=:d, xaxis="Time t", title="Solution to the pendulum ODE with ($n points)", label="odeint")
    for (method, m) in zip(methods, markers)
        sol = method(f_pend, y0, t)
        plot!(t, sol[:, 1], marker=m, label=string(method))
    end
    display(plt)
end

test_1(10)

test_1(20)

test_1(100)

test_1(200)

y0 = [0; 1; 0.1]

function f(y, t)
    return [y[2], y[3], 12 * y[1]^(4/5) + cos(y[2])^3 - sin(y[3])]
end

function f_2(t, y, dy)
    dy[1] = y[2]
    dy[2] = y[3]
    dy[3] = 12 * y[1]^(4/5) + cos(y[2])^3 - sin(y[3])
end

function test_2(n=101)
    t = linspace(0, 1, n)
    tspan = (0.0, 1.0)
    t1, sol = odeint_1(f_2, y0, tspan)
    plt = plot(t1, sol[:, 1], marker=:d, xaxis="Time t", title="Solution to an ODE with ($n points)", label="odeint")
    for (method, m) in zip(methods, markers)
        sol = method(f, y0, t)
        plot!(t, sol[:, 1], marker=m, label=string(method))
    end
    display(plt)
end

test_2(10)

test_2(50)

y0 = [10.0, -3.0, 1.0, 1.0]

function f(y, t)
    return [y[2], y[3], y[4], y[1]^(-5/3)]
end

function f_2(t, y, dy)
    dy[1] = y[2]
    dy[2] = y[3]
    dy[3] = y[4]
    dy[4] = y[1]^(-5/3)
end

function test_3(n=101)
    t = linspace(0, 1, n)
    tspan = (0.0, 1.0)
    t1, sol = odeint_1(f_2, y0, tspan)
    plt = plot(t1, sol[:, 1], marker=:d, xaxis="Time t", title="Solution to an ODE with ($n points)", label="odeint")
    for (method, m) in zip(methods, markers)
        sol = method(f, y0, t)
        plot!(t, sol[:, 1], marker=m, label=string(method))
    end
    display(plt)
end

test_3(10)

test_3(50)

function benchmark(n=101)
    t = linspace(0, 1, n)
    tspan = (0.0, 1.0)

    print("Time of solving an ODE with the 'solve' method from 'DifferentialEquations' ...\n")
    @time t1, sol = odeint_1(f_2, y0, tspan)
    for method in methods
        print("Time of solving an ODE with the $method method for $n points ...\n")
        @time sol = method(f, y0, t)
    end
end

for n in [20, 100, 1000]
    print("\nFor $n points...\n")
    benchmark(n)
end

using BenchmarkTools, Compat

function benchmark(n=101)
    t = linspace(0, 1, n)
    tspan = (0.0, 1.0)

    print("Time of solving an ODE with the 'solve' method from 'DifferentialEquations' ...\n")
    @btime t1, sol = $odeint_1($f_2, $y0, $tspan)
    for method in methods
        print("Time of solving an ODE with the $method method for $n points ...\n")
        @btime sol = $method($f, $y0, $t)
    end
end

for n in [20, 100, 1000]
    print("\nFor $n points...\n")
    benchmark(n)
end
