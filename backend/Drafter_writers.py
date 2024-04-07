from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
import json
class DraftWriter:
    def __init__(self):
        self.llm = Ollama(model="Noun-Hermes-2:4q" , temperature=0)
    def template(self,system, instruction, example, expected_output, input):
        tamplate = PromptTemplate.from_template("""
            <system>
            {system}
            </system>
            <instruction>
            {instruction}                     
            </instruction>
            <input example>
            {example}                      
            </input example>
            <expected_output>
            {expected_output}
            </expected_output>
            <input>                                           
            {input}
            </input>                                    
        """
        )
        return tamplate
    def clean_output(self,output):
        try:
            clean_output = output.replace("<|im_end|>", "").strip()
            return clean_output
        except:
            return output
        
    def launcher(self,input):
        system = "Create Summarize of the review from the customer and give the rating of the review Rating is between 1 to 5, then create a draft for the review in Json Format without explanation."
        instruction = "Clearly mention the rating of the review and summarize the review.\
            \n\nFor example, if the review is about a restaurant, you can mention the food quality, service, and ambiance.\
            \n\nIf the review is about a product, you can mention the quality, durability, and price.\
            \n\nIf the review is about a service, you can mention the quality of the service, the professionalism of the staff, and the overall experience."

        example = "Review: The food was delicious and the service was excellent. I would definitely recommend this restaurant to my friends.\
            \n\nRating: 5/5 "

        expected_output = """
        {
            "Topic": "Restaurant Review",
            "Rating": 5,
            "Summary": "The food was delicious and the service was excellent. I would definitely recommend this restaurant to my friends."
        }
        """
        chain = self.template(system, instruction, example, expected_output, input) | self.llm
        output = chain.invoke({"system": system, "instruction": instruction, "example": example, "expected_output": expected_output, "input": input})
        output = self.clean_output(output)
        with open("draft.json", "w") as file:
            file.write(output)
        result = json.loads(output)

        return result

# result = DraftWriter().launcher("""This image shows a screenshot of a review for a company named "GREAT LITTLE BIKE". The review is written by a customer who expresses their disappointment and discontent with the company's service. Here's an analysis of the comment:

# 1. **Positive Mention**: The customer mentions that the product (a bike) was delivered quickly, which is a positive aspect of the service provided by the company.

# 2. **Negative Feedback**: The majority of the review details negative experiences with the company. The customer indicates that their experience with customer service was not pleasant. They mention that they feel ignored and undervalued, suggesting a lack of communication or empathy from the company's representatives.

# 3. **Issues with Complaints**: The customer points out that their complaints have been met with nonchalance, which implies that the company has not effectively addressed their concerns or provided satisfactory solutions to the issues they raised.

# 4. **Lack of Resolution**: The customer expresses frustration over a lack of resolution regarding their complaints. They mention that their attempts to reach out for assistance have not yielded any positive results.

# 5. **Potential for Future Business**: The review implies that if the company were to provide better customer service, the customer might be inclined to return as a customer in the future. However, given the current experience, this is unlikely.

# 6. **Impact on Reputation**: This negative review could impact the reputation of the company, particularly if there are other similar reviews from customers who have had similar experiences. It suggests that the company needs to improve its customer service processes and perhaps consider offering additional support to resolve issues more effectively.

# 7. **Call for Improvement**: The review serves as a call to action for the company to address the issues raised by the customer, in hopes of improving customer satisfaction and retention.

# 8. **Potential for Recovery**: The last sentence of the review suggests that there is still hope for recovery if the company takes steps to rectify the situation.

# To improve in this area, the company might consider implementing better communication channels, training its staff on effective customer service, and actively addressing and resolving customer complaints promptly and professionally. """)

# print(result["Rating"])