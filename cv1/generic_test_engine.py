
import sys

def generic_test_engine(input_matrix, callback, limit=sys.maxsize, postprocess=None, unpack=False):
    """
    : unpack=True interpretuje prvy argument ako pole jednotlivych argumentov predatelnych funkcii [a,b,c] -> f(a,b,c)
    """
    statuses = []
    no_all = 0
    no_correct = 0

    for i, single_test_case in enumerate(input_matrix):
        if i == limit: break

        test_case_in = single_test_case[0]
        test_case_correct_out = single_test_case[1]

        if not unpack:
            tested_function_output = callback(test_case_in)
        if unpack:
            tested_function_output = callback(*test_case_in)

        no_all += 1
        if postprocess is not None:
            tested_function_output_postprocessed = postprocess(tested_function_output)
        else:
            tested_function_output_postprocessed = tested_function_output

        # co ak sme zabudli pretypovat? Toto nas upozorni!
        if type(tested_function_output_postprocessed) != type(test_case_correct_out):
            statuses.append('[WARNING] types of compared variables are NOT same')

        if tested_function_output_postprocessed == test_case_correct_out:
            statuses.append("{} OK".format(i))
            no_correct += 1

        else:
            statuses.append("{index} FAILED In: {test_case_in} \n Our: {our} \n Correct: {correct}".format(
                index=i,
                test_case_in=test_case_in,
                our=tested_function_output,
                correct=test_case_correct_out
            )
            )

    print("""
         ----------------------------------------------------
         RESULT {no_correct}/{no_all} passed.
         ----------------------------------------------------
    """.format(
        no_correct=no_correct,
        no_all=no_all

    ))

    print("\n".join(statuses))