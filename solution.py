def sort_emotions(arr, order):
    emotions = {
        ":D": 5,
        ":)": 4,
        ":|": 3,
        ":(": 2,
        "T_T": 1,
    }

    arr.sort(key=lambda x: emotions[x], reverse=order)
    return arr
  
 
import codewars_test as test
from solution import sort_emotions

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Descending")
    def descending_order_tests():
        test.assert_equals(sort_emotions([ ':D', 'T_T', ':D', ':(' ], True), [ ':D', ':D', ':(', 'T_T' ])
        test.assert_equals(sort_emotions([ 'T_T', ':D', ':(', ':(' ], True), [ ':D', ':(', ':(', 'T_T' ])
        test.assert_equals(sort_emotions([ ':)', 'T_T', ':)', ':D', ':D' ], True), [ ':D', ':D', ':)', ':)', 'T_T' ])

    @test.it("Ascending")
    def ascending_order_tests():
        test.assert_equals(sort_emotions([ ':D', 'T_T', ':D', ':(' ], False), [ 'T_T', ':(', ':D', ':D' ])
        test.assert_equals(sort_emotions([ 'T_T', ':D', ':(', ':(' ], False), [ 'T_T', ':(', ':(', ':D' ])
        test.assert_equals(sort_emotions([ ':)', 'T_T', ':)', ':D', ':D' ], False),  [ 'T_T', ':)', ':)', ':D', ':D' ])

    @test.it("Empty array")
    def empty_array_tests():
        test.assert_equals(sort_emotions([], False), [])
        test.assert_equals(sort_emotions([], True), [])
