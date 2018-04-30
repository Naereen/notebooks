
A = [ 1. 2 3; 4 5 6; 7 8 9 ]

B = [12 -51 4; 6 167 -68; -4 24 -41]

function check_DV(A, D, V)
    I = eye(size(A)[1])
    for i = 1:size(A)[1]
        check = (A - D[i] * I) * V[:,i]
        println("For the ", i, "th eigen value and vector, (A - lambda I)^k * v = ", check, "\n\twhich has a L2 norm = ", norm(check))
        assert(norm(check) <= 1e-14)
    end
end

D_A, V_A = eig(A)

check_DV(A, D_A, V_A)

D_B, V_B = eig(B)

check_DV(B, D_B, V_B)

"Power iteration method on A, to find eigenpair with largest eigen value."
function poweriteration(A, maxiter=20, userandomstart=true)
    n = size(A)[1]
    if userandomstart
        X = randn((n, 1))
    else
        X = ones((n, 1))
    end
    for i = 1:maxiter
        next_X = A * X
        X = next_X / norm(next_X)
    end
    # lambda = (X^* ⋅ A ⋅ X) / (X^* ⋅ X)
    lambda = (transpose(conj(X)) * (A * X)) / (transpose(conj(X)) * X)
    lambda, X
end

poweriteration(A)

D_A, V_A = eig(A)

(D_A[1], -1 * V_A[:,1])

poweriteration

println(poweriteration(A, 1))
println(poweriteration(A, 2))
println(poweriteration(A, 5))
println(poweriteration(A, 10))

"Inner product of two vectors v, w. Can be vertical (n,1) or horizontal (1,n) vectors."
function inner(v, w)
    assert(size(v) == size(w))
    nm = size(v)
    if length(nm) == 1
        return transpose(conj(v)) * w
    elseif nm[1] == 1
        return conj(v) * transpose(w)
    end
end

inner([1 1 1], [2 3 4])

inner([1; 1; 1], [2; 3; 4])

"projection(a, e): projection operator of vector a onto base vector e. Uses inner(e, a) and inner(e, e)."
function projection(a, e)
    return (inner(e, a) / inner(e, e)) * e 
end

"gramschmidt(A): Gram-Schmidt orthogonalization operator, returns us, es (unormalized matrix, base matrix)."
function gramschmidt(A, verbose=false)
    assert(size(A)[1] == size(A)[2])
    n = size(A)[1]
    if verbose
        println("n = ", n)
    end
    us = zeros((n, n))
    es = zeros((n, n))
    for i = 1:n
        if verbose
            println("i = ", i)
        end
        us[:,i] = A[:,i] 
        for j = 1:i-1
            if verbose
                println("\tj = ", j)
                println("\tus[:,i] = ", us[:,i])
            end
            us[:,i] -= projection(A[:,i], us[:,j]) 
        end
        if verbose
            println("us[:,i] = ", us[:,i])
        end
        es[:,i] = us[:,i] / norm(us[:,i])
        if verbose
            println("es[:,i] = ", es[:,i])
        end
    end
    return us, es
end

A

us, es = gramschmidt(A)

us

es

inner(es[:,1], A[:,1]) * es[:,1]

inner(es[:,1], A[:,2]) * es[:,1] + inner(es[:,2], A[:,2]) * es[:,2]

rank(A)

inner(es[:,1], A[:,3]) * es[:,1] + inner(es[:,2], A[:,3]) * es[:,2] + inner(es[:,3], A[:,3]) * es[:,3]

[ norm(es[:,i]) for i = 1:size(es)[1] ]

(es' * es)[1:2,1:2]

us, es = gramschmidt(B)

[ norm(es[:,i]) for i = 1:size(es)[1] ]

es * es'

V = [3 2; 1 2]

us, es = gramschmidt(V)

es' * es

"QR decomposition, returns (Q, R): Q is orthogonal and R is upper-triangular, such that A = Q R."
function QR(A)
    assert(size(A)[1] == size(A)[2])
    n = size(A)[1]
    us, es = gramschmidt(A)
    Q = copy(es)
    R = zeros((n, n))
    for i = 1:n
        for j = i:n
            R[i,j] = inner(es[:,i], A[:,j])
        end
    end
    return Q, R
end

Q, R = QR(A)

A

Q

R

Q * R

Q2, R2 = QR(B)

B

Q2

R2

Q2 * R2

B == Q2 * R2

assert(norm(B - (Q2 * R2)) <= 1e-13)

"Apply the QR method for maxiter steps. Should return a triangular matrix similar to A (same eigenvalues)."
function QR_method(A, maxiter=50)
    Ak = A
    for k = 1:maxiter
        Qk, Rk = QR(Ak)
        Ak = Rk * Qk
    end
    return Ak
end

Ak = QR_method(A)

"Truncate to zero values under the diagonal (have to be smaller than tolerance)"
function truncate_to_zero_below_diag(A, tolerance=1e-12)
    assert(size(A)[1] == size(A)[2])
    n = size(A)[1]
    for j = 1:n
        for i = j+1:n
            assert(norm(A[i,j]) <= tolerance)
            A[i,j] = 0
        end
    end
    return A
end

truncate_to_zero_below_diag(Ak)

Ak = QR_method(B)

truncate_to_zero_below_diag(Ak)

"Extract the diagonal from the QR method."
function QR_eigenvalues(A, maxiter=50)
    return diag(QR_method(A, maxiter))
end

QR_eigenvalues(A)

eigvals(A)

QR_eigenvalues(B)

eigvals(B)

"Inverse iteration method to find the eigen vector corresponding to a given eigen value."
function inverseIteration(A, val, maxiter=20, userandomstart=true)
    mu_I = val * eye(A)
    inv_A_minus_muI = inv(A - mu_I)
    n = size(A)[1]
    if userandomstart
        X = randn((n, 1))
    else
        X = ones((n, 1))
    end
    for i = 1:maxiter
        next_X = inv_A_minus_muI * X
        X = next_X / norm(next_X)
    end
    X
end

"Approximation of D, V: D contains the eigen values (vector) and V the eigen vectors (column based)."
function QR_eigen(A, maxiter=20, userandomstart=true)
    n = size(A)[1]
    D = QR_eigenvalues(A, maxiter)
    V = zeros((n,n))
    for i = 1:n
        V[:,i] = inverseIteration(A, D[i], maxiter, userandomstart)
    end
    return D, V
end

D2, V2 = QR_eigen(B)

D2s, V2s = eig(B)
