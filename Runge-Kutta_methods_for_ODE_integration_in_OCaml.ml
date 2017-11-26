(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#Runge-Kutta-methods-for-ODE-integration-in-OCaml" data-toc-modified-id="Runge-Kutta-methods-for-ODE-integration-in-OCaml-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Runge-Kutta methods for ODE integration in OCaml</a></div><div class="lev2 toc-item"><a href="#Preliminary" data-toc-modified-id="Preliminary-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Preliminary</a></div><div class="lev2 toc-item"><a href="#Runge-Kutta-method-of-order-1,-or-the-Euler-method" data-toc-modified-id="Runge-Kutta-method-of-order-1,-or-the-Euler-method-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Runge-Kutta method of order 1, or the Euler method</a></div><div class="lev2 toc-item"><a href="#Runge-Kutta-method-of-order-2" data-toc-modified-id="Runge-Kutta-method-of-order-2-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Runge-Kutta method of order 2</a></div><div class="lev2 toc-item"><a href="#Runge-Kutta-method-of-order-4,-&quot;RK4&quot;" data-toc-modified-id="Runge-Kutta-method-of-order-4,-&quot;RK4&quot;-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Runge-Kutta method of order 4, <em>"RK4"</em></a></div><div class="lev2 toc-item"><a href="#Comparisons" data-toc-modified-id="Comparisons-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Comparisons</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Conclusion</a></div> *)

(* # Runge-Kutta methods for ODE integration in OCaml

- I want to implement and illustrate the [Runge-Kutta method](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods) (actually, different variants), in the [OCaml programming language](https://www.ocaml.org/).

- The Runge-Kutta methods are a family of numerical iterative algorithms to approximate solutions of [Ordinary Differential Equations](https://en.wikipedia.org/wiki/Ordinary_differential_equation). I will simply implement them, for the mathematical descriptions, I let the interested reader refer to the Wikipedia page, or [any](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods#References) [good](https://www.directtextbook.com/isbn/9780521007948) [book](https://www.decitre.fr/livres/analyse-numerique-et-equations-differentielles-9782868838919.html) or [course](https://courses.maths.ox.ac.uk/node/4294) on numerical integration of ODE.
- I will start with the order 1 method, then the order 2 and the most famous order 4.
- They will be compared on different ODE. *)

(* ## Preliminary *)

(* In[1]: *)


Sys.command "ocaml -version";;

(* In[147]: *)


#thread ;;
#require "jupyter.notebook" ;;
#require "jupyter.archimedes" ;;

(* I don't want to try to find a reference implementation of an Ordinary Differential Equations solver in OCaml. I'm sure there is, just don't care. *)

(* I will use as a first example the one included in [the scipy (Python) documentation for this `odeint` function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html).

$$\theta''(t) + b \theta'(t) + c \sin(\theta(t)) = 0.$$

If $\omega(t) := \theta'(t)$, this gives
$$ \begin{cases}
\theta'(t) = \omega(t) \\
\omega'(t) = -b \omega(t) - c \sin(\theta(t))
\end{cases} $$

Vectorially, if $y(t) = [\theta(t), \omega(t)]$, then the equation is $y' = f(t, y)$ where $f(t, y) = [y_2(t), -b y_2(t) - c \sin(y_1(t))]$. *)

(* We assume the values of $b$ and $c$ to be known, and the starting point to be also fixed: *)

(* In[11]: *)


let b = 0.25 ;;
let c = 5.0 ;;

(* In[14]: *)


let y0 = [| 3.14156 -. 0.1; 0.0 |];;

(* In[148]: *)


let f_pend (y : float array) (_ : float) : float array =
    [|
        y.(1);
        (-.b) *. y.(1) +. (-.c) *. sin(y.(0))
    |]
;;

(* ----
## Runge-Kutta method of order 1, or the Euler method *)

(* The approximation is computed using this update:
$$y_{n+1} = y_n + (t_{n+1} - t_n) f(y_n, t_n).$$

The math behind this formula are the following: if $g$ is a solution to the ODE, and so far the approximation is correct, $y_n \simeq g(t_n)$, then a small step $h = t_{n+1} - t_n$ satisfy $g(t_n + h) \simeq g(t_n) + h g'(t_n) \simeq y_n + h f(g(t_n), t_n) + \simeq y_n + h f(y_n, t_n)$. *)

(* In[32]: *)


let rungekutta1 (f : float array -> float -> float array) (y0 : float array) (t : float array) =
    let d = Array.length y0 in
    let n = Array.length t in
    let y = Array.make_matrix n d 0. in
    for j   = 0 to d-1 do
        y.(0).(j) <- y0.(j);
    done;
    for i = 0 to n-2 do
        let h   = t.(i+1) -. t.(i) in
        let fyt = f y.(i) t.(i) in
        for j   = 0 to d-1 do
            y.(i+1).(j) <- y.(i).(j) +. h *. fyt.(j);
        done;
    done;
    y
;;

(* We have to redefine ourselfves most of the useful functions: *)

(* In[28]: *)


let linspace (a : float) (b : float) (n : int) =
    let t = Array.make n a in
    let h = (b -. a) /. (float_of_int n) in
    for i = 0 to n-1 do
        t.(i) <- a +. (float_of_int i) *. h;
    done;
    t
;;

(* In[30]: *)


let t = linspace 0. 10. 101 ;;

(* In[31]: *)


let sol = rungekutta1 f_pend y0 t ;;

(* In[34]: *)


let column sol i =
    Array.map (fun x -> x.(i)) sol
;;

(* Let see a first plot! *)

(* In[151]: *)


let vp = A.init ~w:800. ~h:360. ["jupyter"] in
A.Axes.box vp ;
A.Viewport.xlabel vp "Time t";
A.Viewport.title vp "Solution to the pendulum ODE with Runge-Kutta 1";
A.set_color vp A.Color.red ;
A.Viewport.text vp 7. 3. "o theta(t)" ;
A.Array.xy ~style:(`Linesmarkers "o") vp t (column sol 0);
A.set_color vp A.Color.blue ;
A.Viewport.text vp 7. 2.5 "+ omega(t)" ;
A.Array.xy ~style:(`Linesmarkers "+") vp t (column sol 1);
A.close vp;;

(* With the same number of points, the Euler method (*i.e.* the Runge-Kutta method of order 1) is less precise than the reference `solve` method. With more points, it can give a satisfactory approximation of the solution: *)

(* In[55]: *)


let t = linspace 0. 10. 1001 ;;
let sol = rungekutta1 f_pend y0 t ;;

(* In[153]: *)


let vp = A.init ~w:800. ~h:360. ["jupyter"] in
A.Axes.box vp ;
A.Viewport.xlabel vp "Time t";
A.Viewport.title vp "Solution to the pendulum ODE with Runge-Kutta 1";
A.set_color vp A.Color.red ;
A.Viewport.text vp 8.5 3. "o theta(t)" ;
A.Array.xy ~style:(`Linesmarkers "o") vp t (column sol 0);
A.set_color vp A.Color.blue ;
A.Viewport.text vp 8.5 2.5 "+ omega(t)" ;
A.Array.xy vp ~style:(`Linesmarkers "+") t (column sol 1);
A.close vp;;

(* In[72]: *)


let t = linspace 0. 10. 10001 ;;
let sol = rungekutta1 f_pend y0 t ;;

(* In[154]: *)


let vp = A.init ~w:800. ~h:360. ["jupyter"] in
A.Axes.box vp ;
A.Viewport.xlabel vp "Time t";
A.Viewport.title vp "Solution to the pendulum ODE with Runge-Kutta 1";
A.set_color vp A.Color.red ;
A.Viewport.text vp 8.5 3. "o theta(t)" ;
A.Array.xy ~style:(`Linesmarkers "o") vp t (column sol 0);
A.set_color vp A.Color.blue ;
A.Viewport.text vp 8.5 2.5 "+ omega(t)" ;
A.Array.xy vp ~style:(`Linesmarkers "+") t (column sol 1);
A.close vp;;

(* ----
## Runge-Kutta method of order 2 *)

(* The order 2 Runge-Method uses this update:
$$ y_{n+1} = y_n + h f(t + \frac{h}{2}, y_n + \frac{h}{2} f(t, y_n)),$$
if $h = t_{n+1} - t_n$. *)

(* Again, we need some basic functions as OCaml `Array` are quite poor.
With Julia arrays or NumPy Python arrays, we can write `h * f(y, t)` to multiply each entry of `f(y, t)` by a number h. *)

(* In[92]: *)


let aplus a k =
    Array.map ( ( +. ) k) a
;;

let ( ++. ) = aplus ;;

(* In[93]: *)


let aaplus a b =
    Array.map2 ( +. ) a b
;;

let ( +++. ) = aaplus ;;

(* In[94]: *)


let amul a k =
    Array.map ( ( *. ) k ) a
;;

let ( **. ) = amul ;;

(* In[95]: *)


let rungekutta2 (f : float array -> float -> float array) (y0 : float array) (t : float array) =
    let d = Array.length y0 in
    let n = Array.length t in
    let y = Array.make_matrix n d 0. in
    for j = 0 to d-1 do
        y.(0).(j) <- y0.(j);
    done;
    for i = 0 to n-2 do
        let h    = t.(i+1) -. t.(i) in
        let fyt  = f y.(i) t.(i) in
        let fyt2 = f (y.(i) +++. (fyt **. (h /. 2.))) (t.(i) +. (h /. 2.)) in
        for j    = 0 to d-1 do
            y.(i+1).(j) <- y.(i).(j) +. h *. fyt2.(j);
        done;
    done;
    y
;;

(* For our simple ODE example, this method is already quite efficient. *)

(* In[87]: *)


let t = linspace 0. 10. 101 ;;
let sol = rungekutta2 f_pend y0 t ;;

(* In[156]: *)


let vp = A.init ~w:800. ~h:360. ["jupyter"] in
A.Axes.box vp ;
A.Viewport.xlabel vp "Time t";
A.Viewport.title vp "Solution to the pendulum ODE with Runge-Kutta 2";
A.set_color vp A.Color.red ;
A.Viewport.text vp 8.5 3. "o theta(t)" ;
A.Array.xy ~style:(`Linesmarkers "o") vp t (column sol 0);
A.set_color vp A.Color.blue ;
A.Viewport.text vp 8.5 2.5 "+ omega(t)" ;
A.Array.xy vp ~style:(`Linesmarkers "+") t (column sol 1);
A.close vp;;

(* ----
## Runge-Kutta method of order 4, *"RK4"* *)

(* The order 4 Runge-Method uses this update:
$$ y_{n+1} = y_n + \frac{h}{6} (k_1 + 2 k_2 + 2 k_3 + k_4),$$
if $h = t_{n+1} - t_n$, and
$$\begin{cases}
k_1 &= f(y_n, t_n), \\
k_2 &= f(y_n + \frac{h}{2} k_1, t_n + \frac{h}{2}), \\
k_3 &= f(y_n + \frac{h}{2} k_2, t_n + \frac{h}{2}), \\
k_4 &= f(y_n + h k_3, t_n + h).
\end{cases}$$ *)

(* In[97]: *)


let rungekutta4 (f : float array -> float -> float array) (y0 : float array) (t : float array) =
    let d = Array.length y0 in
    let n = Array.length t in
    let y = Array.make_matrix n d 0. in
    for j = 0 to d-1 do
        y.(0).(j) <- y0.(j);
    done;
    for i = 0 to n-2 do
        let h  = t.(i+1) -. t.(i) in
        let k1 = f y.(i) t.(i) in
        let k2 = f (y.(i) +++. (k1 **. (h /. 2.))) (t.(i) +. (h /. 2.)) in
        let k3 = f (y.(i) +++. (k2 **. (h /. 2.))) (t.(i) +. (h /. 2.)) in
        let k4 = f (y.(i) +++. (k3 **. h)) (t.(i) +. h) in
        for j  = 0 to d-1 do
            y.(i+1).(j) <- y.(i).(j) +. (h/.6.) *. (k1.(j) +. 2.*.k2.(j) +. 2.*.k3.(j) +. k4.(j));
        done;
    done;
    y
;;

(* For our simple ODE example, this method is even more efficient. *)

(* In[107]: *)


let t = linspace 0. 10. 31 ;;
let sol = rungekutta4 f_pend y0 t ;;

(* In[157]: *)


let vp = A.init ~w:800. ~h:360. ["jupyter"] in
A.Axes.box vp ;
A.Viewport.xlabel vp "Time t";
A.Viewport.title vp "Solution to the pendulum ODE with Runge-Kutta 4 (31 points)";
A.set_color vp A.Color.red ;
A.Viewport.text vp 8.5 3. "o theta(t)" ;
A.Array.xy ~style:(`Linesmarkers "o") vp t (column sol 0);
A.set_color vp A.Color.blue ;
A.Viewport.text vp 8.5 2.5 "+ omega(t)" ;
A.Array.xy vp ~style:(`Linesmarkers "+") t (column sol 1);
A.close vp;;

(* In[109]: *)


let t = linspace 0. 10. 101 ;;
let sol = rungekutta4 f_pend y0 t ;;

(* In[158]: *)


let vp = A.init ~w:800. ~h:360. ["jupyter"] in
A.Axes.box vp ;
A.Viewport.xlabel vp "Time t";
A.Viewport.title vp "Solution to the pendulum ODE with Runge-Kutta 4 (101 points)";
A.set_color vp A.Color.red ;
A.Viewport.text vp 8.5 3. "o theta(t)" ;
A.Array.xy ~style:(`Linesmarkers "o") vp t (column sol 0);
A.set_color vp A.Color.blue ;
A.Viewport.text vp 8.5 2.5 "+ omega(t)" ;
A.Array.xy vp ~style:(`Linesmarkers "+") t (column sol 1);
A.close vp;;

(* ----
## Comparisons *)

(* In[120]: *)


let methods = [|rungekutta1; rungekutta2; rungekutta4|] ;;
let names = [|"Runge-Kutta 1"; "Runge-Kutta 2"; "Runge-Kutta 4"|] ;;
let markers = [|"o"; "s"; ">"|] ;;
let colors = [|A.Color.red; A.Color.blue; A.Color.green|] ;;

(* In[159]: *)


let test_1 ?(n=101) () =
    let t = linspace 0. 10. n in
    let vp = A.init ~w:800. ~h:360. ["jupyter"] in
    A.Axes.box vp ;
    A.Viewport.xlabel vp "Time t";
    A.Viewport.title vp (Format.sprintf "Solution to the pendulum ODE with different methods (%i points)" n);
    for i = 0 to (Array.length methods) - 1 do
        let sol = methods.(i) f_pend y0 t in
        A.set_color vp colors.(i);
        A.Viewport.text vp 6.5 (2. -. 2.*.(float_of_int i)) (Format.sprintf "%s %s" markers.(i) names.(i)) ;
        A.Array.xy ~style:(`Linesmarkers markers.(i)) vp t (column sol 0);
    done;
    A.close vp;
;;

(* In[160]: *)


test_1 ~n:10 ();;

(* In[161]: *)


test_1 ~n:30 ();;

(* In[162]: *)


test_1 ~n:100 ();;

(* ## Conclusion

> *That's it for today, folks!* See my other notebooks, [available on GitHub](https://github.com/Naereen/notebooks/). *)
