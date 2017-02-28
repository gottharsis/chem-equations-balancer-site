require 'katex'
def solve expression
    left, right = expression.split('->').map(&:strip).map{|side| side.split('+').map(&:strip)}
    coefficients = eval `python #{__dir__}/chem.py "#{expression}"`
    puts coefficients.class
    left.map!{|cmpd| latex cmpd, coefficients.shift}
    right.map!{|cmpd| latex cmpd, coefficients.shift}
    eqn = left.join(' + ') + ' \rightarrow ' + right.join(' + ')
    Katex.render eqn
end
def latex cmpd, n
    ((n == 1) ? "" : n.to_s) + cmpd.gsub(/(\d+)/, '_{\1}').gsub(/([(])(.*?)(\))/, 'left\1\2right\3')
end
