function J = computeCostMulti(X, y, theta)
%COMPUTECOSTMULTI Compute cost for linear regression with multiple variables
%   J = COMPUTECOSTMULTI(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples
%pred = zeros(m, 1);
%delta = zeros(m, 1);

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

%for i=1:m,
%	pred(i, :) = X(i, :) * theta;
%	delta(i, :) = (pred(i, :) - y(i, :))' * (pred(i, :) - y(i, :));
%end;

%J = (0.5 .* m) .* sum(delta);

%J = (0.5 .* m) .* ((X * theta) - y)' * ((X * theta) - y);

%upd = 0;
%for i=1:m,
%	upd = upd + 0.5/m * sum((theta' * X(i,:)') - y(i)) * X(i,:)';
%end;

%upd

%J = upd;

J=sum((X*theta-y).^2)/(2*m);

% =========================================================================

end
