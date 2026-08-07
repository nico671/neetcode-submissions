class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval_stack = []
        while len(tokens) > 0:
            curr = tokens.pop(0)
            if curr in "+-*/":
                
                snd = eval_stack.pop()
                fst = eval_stack.pop()
                val = 0
                match curr:
                    case "+":
                        val = fst + snd
                    case "-":
                        val = fst - snd
                    case "*":
                        val = fst * snd
                    case "/":
                        if snd != 0:
                            val = fst / snd
                eval_stack.append(int(val))
            else:
                eval_stack.append(int(curr))
            print(eval_stack)
        return eval_stack[-1]