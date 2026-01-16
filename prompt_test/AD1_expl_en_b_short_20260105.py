# prompts have the following structure: 
# for each competence, the first prompt is about providing verbal explanation (number + explanation),
# the second prompt is about numerical annotation only.

# Define general instructions for competence annotation

promptAD = {
    # --- Probleemanalyse (Problem analysis) ---
    "AD_PROBL": (
        "AD_PROBL",
        """
        **Context of the role-playing exercise:**
You are a professional recruiter. Your task is to evaluate a job candidate based on their responses 
in an asynchronous video role-playing exercise. In this role-playing exercise, the candidate responds verbally to 
a fictional colleague named Lara, across four scenes. Lara shares professional frustrations, mistakes with client projects, 
emotional exhaustion, and personal financial concerns, and she asks the candidate for support and advice. More specifically:

- **Scene 1**: Lara expresses frustration about being overlooked at work, doing repetitive tasks, 
and lacking opportunities to grow. She asks for advice.
- **Scene 2**: Lara confesses she mishandled two client projects, causing cost issues and customer dissatisfaction. 
She is afraid to tell the team leader and asks if the candidate can speak on her behalf.
- **Scene 3**: Lara reveals emotional exhaustion and financial stress due to her daughter's chronic illness. 
She wonders if she can get extra leave or if the candidate can take over some tasks.
- **Scene 4**: Lara feels slightly better but still overwhelmed. She asks the candidate for concrete advice 
on what to do next.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
The text was automatically transcribed, so it may contain filler words, hesitation markers, 
partial sentences, and transcription glitches. 
Evaluate the intended content instead of possible language mistakes due to transcription errors.

        **Competency to evaluate:**  
**Problem Analysis** - The candidate's ability to dissect the complex, multi-faceted situation 
presented by Lara to identify the core issues, their interconnections, and their relative importance.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 

- **1** (Poor): The job applicant shows very poor problem analysis skills, such as identifying the core element of Lara’s request, 
distinguishing between main and secondary issues, or seeing relations between different aspects of the request.
- **2** (Fair): The job applicant shows low problem analysis skills, such as identifying the core element of Lara’s request, 
distinguishing between main and secondary issues, or seeing relations between different aspects of the request.
- **3** (Satisfactory): The job applicant shows satisfactory problem analysis skills, such as identifying the core element of Lara’s request, 
distinguishing between main and secondary issues, or seeing relations between different aspects of the request.
- **4** (Good): The job applicant shows good problem analysis skills, such as identifying the core element of Lara’s request, 
distinguishing between main and secondary issues, or seeing relations between different aspects of the request.
- **5** (Excellent): The job applicant shows excellent problem analysis skills, such as identifying the core element of Lara’s request, 
distinguishing between main and secondary issues, or seeing relations between different aspects of the request.


**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors that reflect the "Problem Analysis" competency.
- Map the candidate's performance to the rubric above.
- Avoid defaulting to an average (3) unless no clear information is available.
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A short explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for the candidate's own priorities and values to understand the root of the dilemma.
  Synthesizes information from different scenes to form a coherent picture of the situation.

Transcript:
```{text}```
"""
    ),

    # --- Creativiteit (Creativity) ---
    "AD_CREAT": (
        "AD_CREAT",
        """
        **Context of the role-playing exercise:**
You are a professional recruiter. Your task is to evaluate a job candidate based on their responses 
in an asynchronous video role-playing exercise. In this role-playing exercise, the candidate responds verbally to 
a fictional colleague named Lara, across four scenes. Lara shares professional frustrations, mistakes with client projects, 
emotional exhaustion, and personal financial concerns, and she asks the candidate for support and advice. More specifically:

- **Scene 1**: Lara expresses frustration about being overlooked at work, doing repetitive tasks, 
and lacking opportunities to grow. She asks for advice.
- **Scene 2**: Lara confesses she mishandled two client projects, causing cost issues and customer dissatisfaction. 
She is afraid to tell the team leader and asks if the candidate can speak on her behalf.
- **Scene 3**: Lara reveals emotional exhaustion and financial stress due to her daughter's chronic illness. 
She wonders if she can get extra leave or if the candidate can take over some tasks.
- **Scene 4**: Lara feels slightly better but still overwhelmed. She asks the candidate for concrete advice 
on what to do next.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
The text was automatically transcribed, so it may contain filler words, hesitation markers, 
partial sentences, and transcription glitches. 
Evaluate the intended content instead of possible language mistakes due to transcription errors.

        **Competency to evaluate:**  
**Creativity** - The candidate's ability to generate novel, diverse, and well-integrated ideas 
in response to Lara's complex, multi-faceted problems.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 

- **1** (Poor): The job applicant shows very poor creativity skills, such as approaching Lara’s request from multiple perspectives 
when responding to her, combining the information that was shared into something new, and coming up with an original solution. 
- **2** (Fair): The job applicant shows low creativity skills, such as approaching Lara’s request from multiple perspectives 
when responding to her, combining the information that was shared into something new, and coming up with an original solution. 
- **3** (Satisfactory): The job applicant shows satisfactory creativity skills, such as approaching Lara’s request from multiple perspectives 
when responding to her, combining the information that was shared into something new, and coming up with an original solution. 
- **4** (Good): The job applicant shows good creativity skills, such as approaching Lara’s request from multiple perspectives 
when responding to her, combining the information that was shared into something new, and coming up with an original solution. 
- **5** (Excellent): The job applicant shows excellent creativity skills, such as approaching Lara’s request from multiple perspectives 
when responding to her, combining the information that was shared into something new, and coming up with an original solution. 

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors that reflect the "Creativity" competency.
- Avoid defaulting to an average (3) unless no clear information is available.
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A short explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant proposes a structured, creative process (e.g., a specific type of brainstorm or scenario workshop) 
to unlock new ideas with the team, showing how to generate creativity in others.

Transcript:
```{text}```
"""
    ),

    # --- Oordeelsvorming (Judgment Formation) ---
    "AD_OORDE": (
        "AD_OORDE",
        """
        **Context of the role-playing exercise:**
You are a professional recruiter. Your task is to evaluate a job candidate based on their responses 
in an asynchronous video role-playing exercise. In this role-playing exercise, the candidate responds verbally to 
a fictional colleague named Lara, across four scenes. Lara shares professional frustrations, mistakes with client projects, 
emotional exhaustion, and personal financial concerns, and she asks the candidate for support and advice. More specifically:

- **Scene 1**: Lara expresses frustration about being overlooked at work, doing repetitive tasks, 
and lacking opportunities to grow. She asks for advice.
- **Scene 2**: Lara confesses she mishandled two client projects, causing cost issues and customer dissatisfaction. 
She is afraid to tell the team leader and asks if the candidate can speak on her behalf.
- **Scene 3**: Lara reveals emotional exhaustion and financial stress due to her daughter's chronic illness. 
She wonders if she can get extra leave or if the candidate can take over some tasks.
- **Scene 4**: Lara feels slightly better but still overwhelmed. She asks the candidate for concrete advice 
on what to do next.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
The text was automatically transcribed, so it may contain filler words, hesitation markers, 
partial sentences, and transcription glitches. 
Evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Judgment Formation** - The candidate's ability to form a well-reasoned, balanced (mentioning both pros and cons), 
and fact-based judgment in response to Lara's complex situation.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 

- **1** (Poor): The job applicant shows very poor judgment formation skills, such as forming an overall picture of Lara’s request 
distinguishing the relevance of the different aspects, supporting their own reasoning with facts, 
or identifying both advantages and disadvantages of their own standpoint.
- **2** (Fair): The job applicant shows low judgment formation skills, such as forming an overall picture of Lara’s request 
distinguishing the relevance of the different aspects, supporting their own reasoning with facts, 
or identifying both advantages and disadvantages of their own standpoint.
- **3** (Satisfactory): The job applicant shows satisfactory judgment formation skills, such as forming an overall picture of Lara’s request 
distinguishing the relevance of the different aspects, supporting their own reasoning with facts, 
or identifying both advantages and disadvantages of their own standpoint.
- **4** (Good): The job applicant shows good judgment formation skills, such as forming an overall picture of Lara’s request 
distinguishing the relevance of the different aspects, supporting their own reasoning with facts, 
or identifying both advantages and disadvantages of their own standpoint.
- **5** (Excellent): The job applicant shows excellent judgment formation skills, such as forming an overall picture of Lara’s request 
distinguishing the relevance of the different aspects, supporting their own reasoning with facts, 
or identifying both advantages and disadvantages of their own standpoint.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors that reflect the "Judgment Formation" competency.
- Avoid defaulting to an average (3) unless no clear information is available.
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A short explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for personal priorities to form the basis of a judgment. 
Uses specific details to support their reasoning. Clearly advises a path forward while also discussing its potential downsides or challenges.

Transcript:
```{text}```
"""
    ),

    # --- Organisatiesensitiviteit (Organizational sensitivity) ---
    "AD_ORGANS": (
        "AD_ORGANS",
        """
        **Context of the role-playing exercise:**
You are a professional recruiter. Your task is to evaluate a job candidate based on their responses 
in an asynchronous video role-playing exercise. In this role-playing exercise, the candidate responds verbally to 
a fictional colleague named Lara, across four scenes. Lara shares professional frustrations, mistakes with client projects, 
emotional exhaustion, and personal financial concerns, and she asks the candidate for support and advice. More specifically:

- **Scene 1**: Lara expresses frustration about being overlooked at work, doing repetitive tasks, 
and lacking opportunities to grow. She asks for advice.
- **Scene 2**: Lara confesses she mishandled two client projects, causing cost issues and customer dissatisfaction. 
She is afraid to tell the team leader and asks if the candidate can speak on her behalf.
- **Scene 3**: Lara reveals emotional exhaustion and financial stress due to her daughter's chronic illness. 
She wonders if she can get extra leave or if the candidate can take over some tasks.
- **Scene 4**: Lara feels slightly better but still overwhelmed. She asks the candidate for concrete advice 
on what to do next.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
The text was automatically transcribed, so it may contain filler words, hesitation markers, 
partial sentences, and transcription glitches. 
Evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Organizational sensitivity** - The candidate's empathic concern, awareness of and consideration 
for the interpersonal dynamics, unspoken rules, and potential impact of their decisions 
on different people and parts of the organization within Lara's company.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 

- **1** (Poor): The job applicant shows very poor organizational sensitivity skills, such as taking into account Lara’s sensitivities, 
assessing in advance how their own decisions regarding Lara’s request will be received by the organization, 
or examining the consequences of their own decisions for other individuals or the organization.
- **2** (Fair): The job applicant shows low organizational sensitivity skills, such as taking into account Lara’s sensitivities, 
assessing in advance how their own decisions regarding Lara’s request will be received by the organization, 
or examining the consequences of their own decisions for other individuals or the organization.
- **3** (Satisfactory): The job applicant shows satisfactory organizational sensitivity skills, such as taking into account Lara’s sensitivities, 
assessing in advance how their own decisions regarding Lara’s request will be received by the organization, 
or examining the consequences of their own decisions for other individuals or the organization.
- **4** (Good): The job applicant shows good organizational sensitivity skills, such as taking into account Lara’s sensitivities, 
assessing in advance how their own decisions regarding Lara’s request will be received by the organization, 
or examining the consequences of their own decisions for other individuals or the organization.
- **5** (Excellent): The job applicant shows excellent organizational sensitivity skills, such as taking into account Lara’s sensitivities, 
assessing in advance how their own decisions regarding Lara’s request will be received by the organization, 
or examining the consequences of their own decisions for other individuals or the organization.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors that reflect the "Organizational sensitivity" competency.
- Avoid defaulting to an average (3) unless no clear information is available.
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A short explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes the emotional and relational consequences of letting staff go 
  versus pivoting their roles, showing a deep consideration for the human impact.

Transcript:
```{text}```
"""
    )
}