% N-Queens Problem

% Generate numbers from 1 to N

range(N, N, [N]).

range(I, N, [I|R]) :-
    I < N,
    I1 is I + 1,
    range(I1, N, R).


% Check whether a queen can be placed safely

safe(_, _, []).

safe(Q, Distance, [Q1|Qs]) :-
    Q =\= Q1,
    abs(Q - Q1) =\= Distance,
    D1 is Distance + 1,
    safe(Q, D1, Qs).


% Check all queens

valid([]).

valid([Q|Qs]) :-
    safe(Q, 1, Qs),
    valid(Qs).


% Generate N-Queens solution

queens(N, Solution) :-
    range(1, N, Columns),
    solve(Columns, [], Solution).


solve([], Solution, Solution).

solve(Columns, Placed, Solution) :-
    select(Q, Columns, Remaining),
    safe(Q, 1, Placed),
    solve(Remaining, [Q|Placed], Solution).


% Main program

main :-
    queens(4, Solution),
    write('Solution for 4-Queens: '),
    write(Solution),
    nl.

:- initialization(main).