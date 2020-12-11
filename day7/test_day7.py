from day7.day7 import bagParse, generateRules, simplifyRules, countBags, bagsInBags

testData = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."]

def test_bagParse1():
    assert bagParse(testData[0]) == [["light red",3],["bright white",1],["muted yellow",2]]

def test_bagParse2():
    assert bagParse(testData[1]) == [["dark orange",7],["bright white",3],["muted yellow",4]]

def test_bagParse3():
    assert bagParse(testData[2]) == [["bright white",1],["shiny gold",1]]

def test_bagParse4():
    assert bagParse(testData[3]) == [["muted yellow",11],["shiny gold",2],["faded blue",9]]

def test_bagParse5():
    assert bagParse(testData[4]) == [["shiny gold",3],["dark olive",1],["vibrant plum",2]]

def test_bagParse6():
    assert bagParse(testData[5]) == [["dark olive",7],["faded blue",3],["dotted black",4]]

def test_bagParse7():
    assert bagParse(testData[6]) == [["vibrant plum",11],["faded blue",5],["dotted black",6]]

def test_bagParse8():
    assert bagParse(testData[7]) == [["faded blue",0]]

def test_bagParse9():
    assert bagParse(testData[8]) == [["dotted black",0]]

def test_generateRules():
    assert generateRules(testData) == [[["light red",3],["bright white",1],["muted yellow",2]],
                                      [["dark orange",7],["bright white",3],["muted yellow",4]],
                                      [["bright white",1],["shiny gold",1]],
                                      [["muted yellow",11],["shiny gold",2],["faded blue",9]],
                                      [["shiny gold",3],["dark olive",1],["vibrant plum",2]],
                                      [["dark olive",7],["faded blue",3],["dotted black",4]],
                                      [["vibrant plum",11],["faded blue",5],["dotted black",6]],
                                      [["faded blue",0]],
                                      [["dotted black",0]]]

def test_simpleRules():
    assert simplifyRules(generateRules(testData)) == [["light red","bright white","muted yellow"],
                                                    ["dark orange","bright white","muted yellow"],
                                                    ["bright white","shiny gold"],
                                                    ["muted yellow","shiny gold","faded blue"],
                                                    ["shiny gold","dark olive","vibrant plum"],
                                                    ["dark olive","faded blue","dotted black"],
                                                    ["vibrant plum","faded blue","dotted black"],
                                                    ["faded blue"],
                                                    ["dotted black"]]

def test_countBags():
    assert countBags(generateRules(testData),"shiny gold") == 4

def test_bagsInBags():
    assert bagsInBags(generateRules(testData),"shiny gold") == 32