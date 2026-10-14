% 8-Puzzle using Prolog

% Goal state
goal([1,2,3,4,5,6,7,8,0]).


% Legal moves of blank

% Blank at position 8 -> move RIGHT
move([A,B,C,D,E,F,G,0,I],
     [A,B,C,D,E,F,G,I,0]).

% Blank at position 8 -> move LEFT
move([A,B,C,D,E,F,G,0,I],
     [A,B,C,D,E,F,0,G,I]).

% Blank at position 8 -> move UP
move([A,B,C,D,E,F,G,0,I],
     [A,B,C,D,0,F,G,E,I]).


% Depth-limited search

solve(State, [State,Goal]) :-
    move(State, Goal),
    goal(Goal).


% Print board

print_board([A,B,C,D,E,F,G,H,I]) :-
    write(A), write(' '),
    write(B), write(' '),
    write(C), nl,
    write(D), write(' '),
    write(E), write(' '),
    write(F), nl,
    write(G), write(' '),
    write(H), write(' '),
    write(I), nl.


% Print solution

print_path([]).

print_path([State|Rest]) :-
    print_board(State),
    nl,
    print_path(Rest).


% Main program

main :-
    Initial = [1,2,3,4,5,6,7,0,8],

    write('Initial State:'), nl,
    print_board(Initial),
    nl,

    write('Searching for solution...'), nl,
    nl,

    solve(Initial, Path),

    write('Solution Path:'), nl,
    print_path(Path).


:- initialization(main).