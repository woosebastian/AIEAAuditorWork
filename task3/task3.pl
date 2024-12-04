% https://www.cs.sjsu.edu/~pearce/modules/lectures/prolog/kbase.htm
% https://www.swi-prolog.org/pldoc/man?section=quickstart
% https://www.cs.sjsu.edu/~pearce/modules/lectures/prolog/kbase.htm

% Prolog

engineer(billy).
engineer(joseph).
engineer(sandra).
engineer(mary).
engineer(tim).

works_on_software(billy).
works_on_software(mary).
works_on_software(tim).

works_on_hardware(joseph).
works_on_hardware(sandra).

software_engineer(X) :- engineer(X), works_on_software(X).
hardware_engineer(X) :- engineer(X), works_on_hardware(X).