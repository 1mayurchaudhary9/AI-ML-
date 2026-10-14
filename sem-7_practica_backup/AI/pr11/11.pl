% Travelling Salesperson Problem using Prolog

% Distance between cities

distance(a,b,10).
distance(a,c,15).
distance(a,d,20).

distance(b,a,10).
distance(b,c,35).
distance(b,d,25).

distance(c,a,15).
distance(c,b,35).
distance(c,d,30).

distance(d,a,20).
distance(d,b,25).
distance(d,c,30).


% Calculate cost of a route

route_cost([_], 0).

route_cost([A,B|Rest], Cost) :-
    distance(A,B,D),
    route_cost([B|Rest], C1),
    Cost is D + C1.


% Generate a tour starting and ending at A

tour(Route, Cost) :-
    permutation([b,c,d], P),
    append([a|P], [a], Route),
    route_cost(Route, Cost).


% Find minimum-cost tour

find_best(BestRoute, BestCost) :-
    tour(Route, Cost),
    find_best_route(Route, Cost, BestRoute, BestCost).


find_best_route(Route, Cost, Route, Cost) :-
    \+ (
        tour(R2, Cost2),
        Cost2 < Cost
    ).

find_best_route(Route, Cost, BestRoute, BestCost) :-
    tour(R2, Cost2),
    Cost2 < Cost,
    find_best_route(R2, Cost2, BestRoute, BestCost).


% Main program

main :-
    find_best(Route, Cost),
    write('Optimal Tour: '),
    write(Route),
    nl,
    write('Minimum Cost: '),
    write(Cost),
    nl.


:- initialization(main).