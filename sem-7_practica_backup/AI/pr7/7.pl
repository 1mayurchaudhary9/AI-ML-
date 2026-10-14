% Facts

father(a,b).
father(a,c).
father(b,d).
father(b,e).
father(c,f).

% Brother

brother(X,Y) :-
    father(F,X),
    father(F,Y),
    X \= Y.

% Cousin

cousin(X,Y) :-
    father(F1,X),
    father(F2,Y),
    brother(F1,F2).

% Grandson

grandson(X,Y) :-
    father(Y,F),
    father(F,X).

% Descendent

descendent(X,Y) :-
    father(Y,X).

descendent(X,Y) :-
    father(Y,Z),
    descendent(X,Z).

% Main program

main :-
    write('BROTHER: '),
    findall(X-Y, brother(X,Y), B),
    write(B),
    nl,

    write('COUSIN: '),
    findall(X-Y, cousin(X,Y), C),
    write(C),
    nl,

    write('GRANDSON: '),
    findall(X-Y, grandson(X,Y), G),
    write(G),
    nl,

    write('DESCENDENT: '),
    findall(X-Y, descendent(X,Y), D),
    write(D),
    nl.

:- initialization(main).