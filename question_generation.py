questionTypes = {"What", "How many", "How", "Whom", "Whose", "Who", 
   "When", "Which", "Where", "Why", "Be/Do/etc."}

patternToQuestionType =
  Append[StartOfString | (___ ~~ " ") ~~
       ToLowerCase[#] ~~ ((" " | "," | "s " | "'" | "\"" |
            ":") ~~ __) | (PunctuationCharacter ~~ ("" | " " ...)) ~~
       EndOfString -> # & /@ Most[questionTypes],
   StartOfString ~~ __ ~~ EndOfString -> Last[questionTypes]]]

classifiedQuestions = 
  Map[# -> StringReplace[ToLowerCase[#], 
        patternToQuestionType] &[#] &, 
   Flatten[Normal[
     ResourceData["SQuAD v1.1"][[All, "QuestionAnswerSets"]][[All, 
      All, "Question"]]]]]


