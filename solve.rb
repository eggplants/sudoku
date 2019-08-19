#let change white cell to "0".
problem= `dd`.split("\n").map(&:chars)
if problem.size!=9
    p "line?"
    raise ArgumentError
else if problem.delete_if{|i|i.size!=9}.size!=9
    p "lack of some num?"
    raise ArgumentError
end
problem.each{|i|
    if i.join.chomp.scan(/[^0-9]/)!=0
         p "illegal char?"
         raise ArgunentError
    end
}
