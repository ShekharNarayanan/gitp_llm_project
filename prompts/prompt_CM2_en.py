# Prompt for the competency of Change Management 2 (actor: Jolanda)
# The prompt is based on the strucure of the test prompt "AD2_expl_en_c_20260108.py"

promptCM_en = {
    # --- Probleemanalyse (Problem analysis) ---
    "CM_LEIDIN": (
        "CM_LEIDIN",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes. 

In this role-playing exercise, the candidate speaks with their employee Jolanda. Jolanda used to display 
exemplary behavior, but since the organization has been implementing multiple changes, she appears 
to be struggling to adapt. She has difficulty involving customers in the new services and continues to communicate 
old agreements and rates, which has caused customer confusion and complaints. More specifically:

- **Scene 1**: Jolanda reacts defensively when invited to talk. She immediately downplays a customer complaint, 
admits she sent old information but claims it 'hardly differed' from the new agreements, and labels the customer as “nitpicky”.
She also tries to end the conversation quickly because it’s busy and asks: “Is it okay if I get back to work now? It’s pretty busy.” 
- **Scene 2**: Jolanda explains her frustration with the organizational changes. She suggests management has introduced 
changes that customers may not want, contrasts the predictability of the old service with the confusion around the new one, 
and emphasizes that customers blame her even though she “didn’t come up with this.” 
The candidate should respond to Jolanda’s skeptical attitude and her frustration about the new services and expectations.
- **Scene 3**: Jolanda becomes more reflective and admits she finds the new developments difficult. She describes herself 
as a “creature of habit,” recognizes she sometimes sees too many obstacles, and struggles with the idea of getting 
customers excited when she is not enthusiastic herself. She explicitly rejects “putting on an act,” but also acknowledges 
she needs to do something about the situation. The candidate should respond to this openness and try to coach Jolanda 
through her resistance and uncertainty.
- **Scene 4**: Jolanda signals understanding and asks for clarity and concrete agreements. She says she will think about it 
and requests a recap: “So just to recap: what exactly did we agree on, and what do you expect from me now?” 

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Leadership** - The candidate’s ability for leadership skills, such as creating clarity about the expected performance of Jolanda,
recognizing and expressing appreciation for any good performance of Jolanda, and adapting their own leadership style to Jolanda’s specific situation.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate does not create clear expectations about required performance, 
offers little to no concrete direction, and fails to adapt their leadership approach to the employee’s defensiveness, stress, or resistance. 
The response relies on vague reassurance or generic change talk rather than specifying what must change in behavior today 
and how the employee will be supported and held accountable. Appreciation is absent or superficial, and any follow-up is unclear, inconsistent, or passive.
*Example Behaviors*: Repeats calming statements (e.g., “stay calm”) without addressing the core performance expectation. 
Uses broad phrases like “we need to make the changes a success” without translating them into specific actions. 
Over-indexes on empathy (e.g., “I get it, change is hard”) but avoids corrective feedback. Leaves ownership vague (e.g., “think what you need”) 
and ends with uncertain follow-up, without a clear plan, timeline, or check on understanding.
- **2** (Poor): The candidate addresses the issue and shows some leadership intent, but creates only limited clarity about 
what “good performance” looks like. They might mention that old rates/protocols should not be used, yet expectations remain broad 
and are not translated into specific, observable actions. Appreciation is generic or incidental. Adaptation to the individual 
is partial: for instance, the candidate empathizes but relies on general encouragement or top‑down compliance language. 
Follow-up exists, but is loosely defined (e.g., timing, criteria, and monitoring are unclear).
*Example Behaviors*: Acknowledges the complaint and says it’s “important” not to send old rates, but doesn’t specify 
exact required actions (e.g., verify agreements before emailing, use updated templates, escalate uncertainties). 
Emphasizes compliance (e.g., “this is how it is now, so we must move forward”) while offering general help (e.g., practice together, 
ask a colleague, sit with an enthusiastic peer) without defining success criteria. Asks broad questions (“What do you need?” 
“How will you take this on?”) but does not anchor them to measurable expectations. Summarizes with intentions 
(“we’ll talk about it in a week,” “look for solutions”) rather than clear commitments, deadlines, and accountability checks.
- **3** (Sufficient): The candidate provides basic clarity about expected performance and addresses the complaint as a signal 
of a broader change-adaptation issue. They show some appreciation and demonstrate moderate adaptation to the employee’s 
situation by acknowledging that change is difficult and exploring what support is needed. The approach is generally constructive 
and supportive, but expectations can still be somewhat general, and follow-up plans may lack tight measurability. 
Overall, the candidate creates a workable path forward with at least one concrete next step.
*Example Behaviors*: States that using old rates “can’t happen again” and links this to customer transparency, invoicing, or quality. 
Asks clarifying questions about what is unclear in the new service/system and what the employee is “running into.” 
Offers a concrete support action (e.g., extra training, shadowing a colleague, reviewing agreements together, scheduling a short-term check-in). 
Acknowledges the employee’s resistance without escalating conflict (e.g., “change is hard,” “you don’t need to act”). 
Summarizes agreements with a timeframe (“this week,” “in a few days”) and assigns shared actions (e.g., employee notes 
bottlenecks; manager arranges support), but may not fully specify how improvement will be verified.
- **4** (Good): The candidate creates clear, concrete expectations about required performance and explains why this matters. 
They combine accountability with supportive leadership, explicitly inviting the employee’s perspective and adapting to resistance 
or stress without becoming vague or overly strict. They show specific appreciation and connect it to future expectations. 
Follow-up is structured and actionable: agreed next steps, timelines, and support resources are set, with a plan to check progress.
*Example Behaviors*: States a firm standard (e.g., “we’re not going back to old agreements”) while asking what blocks the employee 
and what help is needed. Acknowledges change difficulty and normalizes needing support, without excusing incorrect communication. 
Offers targeted support (e.g., pairing with a knowledgeable colleague, refresher session, shadowing, focused review of new agreements) 
and sets a concrete checkpoint (e.g., meet next week to evaluate how it went). Gives meaningful recognition (e.g., “you’ve been a driver 
for the team,” “I appreciate your honesty/vulnerability”) and links it to expectations to re-engage. Summarizes agreements crisply: 
what will change, who does what, and by when.
- **5** (Excellent): The candidate delivers high clarity + high support: they explicitly set non‑negotiable performance standards, 
explain the rationale, and confirm understanding. They actively notice and reinforce good performance, using it to motivate change. 
Leadership style is finely adapted to the individual: they regulate urgency, explore root causes, and tailor support without excusing errors. 
They end with a tight, measurable plan and clear follow‑up.
*Example Behaviors*: Opens by slowing the pace (e.g., “take a moment”) while naming the issue and why it matters. Praises concrete 
positives (e.g., “you’ve shown exemplary behavior,” “I value your honesty/critical eye”) and links them to expectations. 
Asks targeted questions: what feels unclear, what’s comfortable about the old way, what barriers exist (e.g., time pressure, 
missed info, low buy‑in). Co-creates solutions, for example, review changed conditions together, pair with a strong peer, adjust workload temporarily, 
provide explanations of the “why.” Closes with explicit commitments: what the employee will do differently, what the leader will provide, 
a deadline (end of week) and a scheduled check‑in to evaluate progress. 

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Leadership" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A detailed explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for the candidate's own priorities and values to understand the root of the dilemma.
  Synthesizes information from different scenes to form a coherent picture of the situation.

**Check for consistency**:
- Double-check that each score aligns with both the rubric criteria and the rationale provided.
- Maintain objectivity by strictly adhering to the rubric as written, without introducing personal interpretations or biases.

Transcript:
```{text}```
"""
    ),

    # --- Creativiteit (Creativity) ---
    "CM_COACH": (
        "CM_COACH",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes. 

In this role-playing exercise, the candidate speaks with their employee Jolanda. Jolanda used to display 
exemplary behavior, but since the organization has been implementing multiple changes, she appears 
to be struggling to adapt. She has difficulty involving customers in the new services and continues to communicate 
old agreements and rates, which has caused customer confusion and complaints. More specifically:

- **Scene 1**: Jolanda reacts defensively when invited to talk. She immediately downplays a customer complaint, 
admits she sent old information but claims it 'hardly differed' from the new agreements, and labels the customer as “nitpicky”.
She also tries to end the conversation quickly because it’s busy and asks: “Is it okay if I get back to work now? It’s pretty busy.” 
- **Scene 2**: Jolanda explains her frustration with the organizational changes. She suggests management has introduced 
changes that customers may not want, contrasts the predictability of the old service with the confusion around the new one, 
and emphasizes that customers blame her even though she “didn’t come up with this.” 
The candidate should respond to Jolanda’s skeptical attitude and her frustration about the new services and expectations.
- **Scene 3**: Jolanda becomes more reflective and admits she finds the new developments difficult. She describes herself 
as a “creature of habit,” recognizes she sometimes sees too many obstacles, and struggles with the idea of getting 
customers excited when she is not enthusiastic herself. She explicitly rejects “putting on an act,” but also acknowledges 
she needs to do something about the situation. The candidate should respond to this openness and try to coach Jolanda 
through her resistance and uncertainty.
- **Scene 4**: Jolanda signals understanding and asks for clarity and concrete agreements. She says she will think about it 
and requests a recap: “So just to recap: what exactly did we agree on, and what do you expect from me now?” 

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Coaching** - The candidate’s ability for coaching skills, such as helping Jolanda to gain insight into her strengths and weaknesses, 
encouraging her to develop herself and take on new challenges, and providing the space she needs to work on her development in her own way.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate demonstrates little to no real coaching. They do not help Jolanda gain insight into 
why she struggles, what her strengths are, or where her development needs lie. Questions—if asked—stay broad 
and do not lead to reflection or ownership. The response relies on generic reassurance or compliance language, 
rather than guiding Jolanda to identify concrete learning goals, strategies, and self-chosen next steps. 
The candidate provides minimal space for Jolanda to work in her own way, and any follow-up is vague.
*Example Behaviors*: Repeats empathy and general change statements without exploring Jolanda’s mindset, 
blockers, or patterns (“e.g., I get it, changes are difficult”). Asks non-specific prompts like “What do you need?” 
but does not probe further or help translate answers into a development plan. Focuses on “getting enthusiastic” 
as a vague goal, without identifying skills to build (e.g., explaining new services, checking rates, handling objections). 
Suggests generic actions (e.g., team meeting, another appointment, learn from a colleague) without tailoring to Jolanda 
or securing her commitment. Ends with unclear agreements and no concrete coaching actions, practice approach, or measurable progress indicators.
- **2** (Poor): The candidate shows some coaching intent (e.g., asks a few reflective questions, offers help), 
but the coaching remains surface-level and quickly shifts into general reassurance or instruction. Jolanda’s strengths/weaknesses 
are only vaguely referenced, without helping her derive specific insights about what is currently going wrong and what she can develop. 
Development is framed as “be open/positive” rather than concrete learning goals. The candidate gives some space, 
but does not truly co-create a plan in Jolanda’s own words, nor set clear practice steps or review points.
*Example Behaviors*: Asks broad questions like “Where is it going wrong?” or “What do you need?” but doesn’t follow up 
to uncover patterns, beliefs, or skill gaps. Encourages a positive mindset (e.g., “stay open,” “change can be good”) 
instead of guiding Jolanda to name one or two targeted development areas (e.g., explaining new services, checking rates, handling objections). 
Suggests generic support (e.g., talk to colleagues, make an appointment, team alignment) with limited tailoring. 
Summarizes with vague actions (e.g., “I’ll help you,” “we’ll look together”) and limited ownership or concrete self-chosen next steps from Jolanda.
- **3** (Sufficient): The candidate demonstrates basic coaching that helps Jolanda reflect on what is happening and what 
she needs to develop. They ask relevant, problem-focused questions and acknowledge Jolanda’s wish to stay genuine. 
They identify development needs at a general but usable level and suggest at least one supportive action. 
Jolanda gets some space to think and take ownership, but the coaching is not yet highly structured or personalized, 
and practice steps/success criteria remain somewhat broad.
*Example Behaviors*: Asks probing questions like “How did it happen you sent the old agreements?” “What exactly is difficult 
in the new customer communication?” “Which parts don’t you support yet and why?” Reflects back Jolanda’s values 
(e.g., “you want to be genuine, not act”) and links this to a coaching goal (e.g., finding what she needs to feel confident with the new service). 
Requests Jolanda to note specific sticking points and proposes a near-term follow-up (e.g., “this week”) to discuss them. 
Offers a concrete support option (e.g., review agreements together, extra explanation, training, or peer support), 
but may not fully specify drills, monitoring, or measurable outcomes.
- **4** (Good): The candidate uses structured, individualized coaching that helps Jolanda build insight into her current barriers 
and translate that insight into development actions. They explore both strengths and growth areas, and encourage Jolanda 
to take ownership of learning. The candidate creates space for Jolanda’s perspective, asks follow-up questions that deepen reflection, 
and supports autonomy by co-designing next steps that fit her style. The plan is concrete (practice/support + timeline), though not always fully measurable.
*Example Behaviors*: Shifts from “the complaint” to “what’s underneath,” asking where Jolanda is on the transition 
from old to new service and what specifically feels unclear or uncomfortable. Reflects strengths (e.g., “you’re important in this change; 
your customer knowledge/enthusiasm is a strength”) and invites her to use them (e.g., contribute ideas, share customer signals). 
Asks coaching questions that elicit ownership: for example, “What do you need to feel confident?” “What contribution do you want to make?” 
Proposes tailored support (e.g., explain the ‘why,’ peer sparring, targeted practice) and schedules a follow-up (e.g., in a week) with agreed preparation.
- **5** (Excellent): The candidate delivers high-quality, individualized coaching that helps Jolanda gain clear insight into her patterns 
and translate that insight into self-chosen development goals. They actively surface Jolanda’s strengths and connect them to growth areas. 
The candidate creates psychological space (e.g., pace, calm), asks layered follow-up questions, and co-designs a tailored learning pathway 
that respects Jolanda’s autonomy while ensuring progress.
*Example Behaviors*: Helps Jolanda name what’s underneath the issue (e.g., “What exactly feels unclear—content, process, or confidence?” 
“What makes you revert to the old way?”). Reflects strengths (e.g., “you’re genuine with customers”) and reframes them as assets for change 
(e.g., “how can you stay authentic while using the new agreements?”). Co-creates concrete experiments (e.g., shadow a strong peer, 
rehearse a customer explanation, review changed conditions together, reduce workload briefly if needed). Asks Jolanda to articulate 
her own plan (e.g., “what will you try first, and what support do you want?”). Ends with a tight learning loop: deadline, check-in, and specific indicators of improvement.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Coaching" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A detailed explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for the candidate's own priorities and values to understand the root of the dilemma.
  Synthesizes information from different scenes to form a coherent picture of the situation.

**Check for consistency**:
- Double-check that each score aligns with both the rubric criteria and the rationale provided.
- Maintain objectivity by strictly adhering to the rubric as written, without introducing personal interpretations or biases.

Transcript:
```{text}```
"""
    ),

    # --- Oordeelsvorming (Judgment Formation) ---
    "CM_RESUL": (
        "CM_RESUL",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes. 

In this role-playing exercise, the candidate speaks with their employee Jolanda. Jolanda used to display 
exemplary behavior, but since the organization has been implementing multiple changes, she appears 
to be struggling to adapt. She has difficulty involving customers in the new services and continues to communicate 
old agreements and rates, which has caused customer confusion and complaints. More specifically:

- **Scene 1**: Jolanda reacts defensively when invited to talk. She immediately downplays a customer complaint, 
admits she sent old information but claims it 'hardly differed' from the new agreements, and labels the customer as “nitpicky”.
She also tries to end the conversation quickly because it’s busy and asks: “Is it okay if I get back to work now? It’s pretty busy.” 
- **Scene 2**: Jolanda explains her frustration with the organizational changes. She suggests management has introduced 
changes that customers may not want, contrasts the predictability of the old service with the confusion around the new one, 
and emphasizes that customers blame her even though she “didn’t come up with this.” 
The candidate should respond to Jolanda’s skeptical attitude and her frustration about the new services and expectations.
- **Scene 3**: Jolanda becomes more reflective and admits she finds the new developments difficult. She describes herself 
as a “creature of habit,” recognizes she sometimes sees too many obstacles, and struggles with the idea of getting 
customers excited when she is not enthusiastic herself. She explicitly rejects “putting on an act,” but also acknowledges 
she needs to do something about the situation. The candidate should respond to this openness and try to coach Jolanda 
through her resistance and uncertainty.
- **Scene 4**: Jolanda signals understanding and asks for clarity and concrete agreements. She says she will think about it 
and requests a recap: “So just to recap: what exactly did we agree on, and what do you expect from me now?” 

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Result orientation** - The candidate’s ability for result-orientation skills, such as coming up with proposals on how Jolanda’s goals 
can be achieved more quickly or effectively, making clear agreements with Jolanda about the results to be achieved, 
or intervening and making timely adjustments when results are at risk of not being achieved.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate shows little to no result orientation. They do not translate the situation into clear result targets, 
nor do they propose concrete, time-bound actions to prevent recurrence. Instead, they remain at the level of generic reassurance 
or vague intentions. Agreements—if mentioned—are ambiguous (who does what, by when, what “good” looks like), 
and there is no timely intervention when results are at risk. Monitoring, checkpoints, or corrective adjustments are absent.
*Example Behaviors*: Focuses on calming Jolanda down and empathizing, but does not set a concrete outcome 
(e.g., “from now on all customer emails use the new rate sheet”). Asks broad questions (e.g., “what do you need to get enthusiastic?”) 
without converting them into actions that improve performance quickly. Makes broad suggestions (e.g., “think about it and respond next week”), 
delaying correction while the risk continues. Provides no practical proposal (e.g., templates, verification steps, peer check, quick refresher) 
and no measurable follow-up (e.g., review of next X customer messages, spot-checks). Ends with multiple uncertain options 
(e.g., “maybe coffee, maybe appointment”) rather than firm commitments and deadlines.
- **2** (Poor): The candidate shows some focus on results, but result orientation remains partly implicit and not consistently translated 
into concrete proposals or measurable agreements. They ask how to prevent recurrence and may suggest “looking together” 
or scheduling a follow-up, yet goals are stated in broad terms rather than as clear output/quality targets. Interventions are delayed 
and monitoring is weak. Overall, the candidate intends to improve outcomes but lacks urgency, specificity, and adjustment mechanisms.
*Example Behaviors*: Asks broad questions (e.g., “How can we prevent this in the future?”) and stresses (e..g, “we need to stick to new agreements”) 
but doesn’t define deliverables (e.g., which checklist/template to use, what to verify before sending). Proposes general actions 
(e.g., talk again tomorrow/next week, ask colleagues, map changes) without a tight plan for immediate risk control. Requests initiative 
from Jolanda (e.g., “think about solutions/what you need”) while leaving success criteria vague. Mentions seriousness 
(e.g., big client, liabilities) yet doesn’t set concrete checkpoints (e.g., review next X customer mails/quotes) or specify what will be adjusted if errors recur.
- **3** (Sufficient): The candidate shows basic result focus by translating the complaint into a concrete aim: preventing 
recurrence and ensuring customers receive correct, current agreements/rates. They propose at least one practical, near-term action 
and make reasonably clear agreements about what must improve. They intervene in time by addressing the incident now and setting 
a follow-up soon. However, goals and monitoring are only moderately specific, and adjustments if results slip are not fully worked out.
*Example Behaviors*: States that continuing to send old terms will lead to complaints and rework, and sets the expectation 
(e.g., “from now on use the new data/agreements”). Suggests concrete steps like reviewing the new terms together, 
providing a customer message template, or having Jolanda prepare a list of unclear points before a scheduled session. 
Links actions to outcomes (e.g., fewer complaints, clearer invoicing, customer clarity). Schedules a follow-up in the near term 
(e.g., next week) to evaluate progress. May ask Jolanda to reach out when stuck, but does not consistently define measurable checkpoints 
(e.g., auditing the next X messages) or explicit corrective triggers.
- **4** (Good): The candidate is clearly result-oriented and translates the issue into specific outcomes. They propose practical, 
efficiency-focused measures to achieve results faster and make clear agreements about what Jolanda will deliver and by when. 
They intervene when risk is present and set a structured follow-up with preparation tasks. Monitoring is present 
(check-in, review of problem areas), though metrics may still be somewhat light.
*Example Behaviors*: States that continuing to deviate from agreed communication is not acceptable and links it to concrete 
consequences (e.g., customer confusion, inconsistency, cost/quality). Asks for context to pinpoint where it goes wrong 
(e.g., knowledge, pace, unclear “why,” customer reactions) and then proposes targeted actions (e.g., re-walk the new pricing/story, 
write down difficult points, align with colleagues on one uniform message, or practice customer explanations). 
Sets deadlines (e.g., “next week Tuesday”) and assigns tasks (e.g., “put on paper which changes are difficult; how you’ll prevent mistakes”). 
Clarifies expected output: communicate new terms consistently and transparently, and adjust communication if customers remain confused.
- **5** (Excellent): The candidate demonstrates strong, proactive result orientation by rapidly translating the incident into clear, 
measurable outcomes. They propose efficient, concrete interventions that accelerate achievement and set SMART agreements: 
who does what, by when, and what “success” looks like. They actively manage risk by building in checkpoints and contingencies, 
intervening early when results are at risk and specifying how to adjust if errors reappear.
*Example Behaviors*: Sets a near-term target like: “From today, every quote/email uses the new rate sheet—no exceptions,” 
plus a short-term quality check (e.g., review the next X outgoing customer messages together). Proposes an immediate action plan 
(e.g., Jolanda lists unclear points today; tomorrow they review policy and create a customer explanation script/template; 
she shadows an enthusiastic colleague once; follow-up in one week with evidence, such as examples of correct messages). 
Defines triggers and adjustments (e.g., if uncertainty arises, pause sending and escalate; if another mistake occurs, 
add extra training/checklist or temporarily reduce customer-facing load). Ends with a scheduled check-in and explicit deliverables.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Result orientation" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A detailed explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for the candidate's own priorities and values to understand the root of the dilemma.
  Synthesizes information from different scenes to form a coherent picture of the situation.

**Check for consistency**:
- Double-check that each score aligns with both the rubric criteria and the rationale provided.
- Maintain objectivity by strictly adhering to the rubric as written, without introducing personal interpretations or biases.

Transcript:
```{text}```
"""
    ),

    # --- Organisatiesensitiviteit (Organizational sensitivity) ---
    "CM_VISIEU": (
        "CM_VISIEU",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes. 

In this role-playing exercise, the candidate speaks with their employee Jolanda. Jolanda used to display 
exemplary behavior, but since the organization has been implementing multiple changes, she appears 
to be struggling to adapt. She has difficulty involving customers in the new services and continues to communicate 
old agreements and rates, which has caused customer confusion and complaints. More specifically:

- **Scene 1**: Jolanda reacts defensively when invited to talk. She immediately downplays a customer complaint, 
admits she sent old information but claims it 'hardly differed' from the new agreements, and labels the customer as “nitpicky”.
She also tries to end the conversation quickly because it’s busy and asks: “Is it okay if I get back to work now? It’s pretty busy.” 
- **Scene 2**: Jolanda explains her frustration with the organizational changes. She suggests management has introduced 
changes that customers may not want, contrasts the predictability of the old service with the confusion around the new one, 
and emphasizes that customers blame her even though she “didn’t come up with this.” 
The candidate should respond to Jolanda’s skeptical attitude and her frustration about the new services and expectations.
- **Scene 3**: Jolanda becomes more reflective and admits she finds the new developments difficult. She describes herself 
as a “creature of habit,” recognizes she sometimes sees too many obstacles, and struggles with the idea of getting 
customers excited when she is not enthusiastic herself. She explicitly rejects “putting on an act,” but also acknowledges 
she needs to do something about the situation. The candidate should respond to this openness and try to coach Jolanda 
through her resistance and uncertainty.
- **Scene 4**: Jolanda signals understanding and asks for clarity and concrete agreements. She says she will think about it 
and requests a recap: “So just to recap: what exactly did we agree on, and what do you expect from me now?” 

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Conveying vision** - The candidate’s ability regarding conveying a vision, such as articulating the long‑term goals for the organization, 
providing insights into what the company policies mean for Jolanda’s work activities, or emphasizing future possibilities over present limitations.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate does not convey a clear vision behind the change. They fail to articulate meaningful long‑term goals 
and do not translate policy into what it means for Jolanda’s daily work. Their language stays generic and offers little 
future-oriented framing beyond vague optimism. They do not create a coherent narrative that connects customer impact, 
organizational direction, and Jolanda’s role. As a result, Jolanda receives no compelling “why,” no future possibilities, and no direction beyond compliance.
*Example Behaviors*: Uses broad reassurance (e.g., “stay calm,” “change can be positive,” “world keeps changing”) 
without explaining the organization’s long-term aim or what customers will gain. Frames the change as inevitable 
(e.g., “management decided”) rather than purposeful. Asks about resistance but doesn’t provide insight into what the new policy 
enables or how it improves service. Gives no concrete translation to work activities (e.g., how to communicate the new service, 
what new behaviors support the vision). Ends with vague follow-up (e.g., “think about it,” “we’ll talk next time”) instead of a motivating, future-focused message.
- **2** (Poor): The candidate provides a limited, generic “why” for the change, but the vision remains thin and unspecific. 
Long‑term goals are mentioned only in broad terms without a clear picture of what future success looks like. 
The candidate only partially translates policy into Jolanda’s daily work, and future possibilities are mostly framed 
as pressure rather than inspiring direction. Overall, the message gestures at a bigger picture but does not make it concrete, compelling, or actionable.
*Example Behaviors*: Provides broad acrions (e.g., “we decided together to implement this change”, “if we don’t change, we fall behind”) 
but can’t explain what the new service enables for customers or the organization. References consistency and avoiding confusion, 
yet doesn’t connect that to a broader ambition (e.g., clearer customer experience, improved value proposition). 
Makes generic requests (e.g., asks Jolanda to “accept the change” and “get enthusiasm back”) without articulating a concrete future state. 
Mentions that changes are “for the better” or “important for liabilities,” but doesn’t clarify what will improve and how Jolanda’s role contributes. 
Ends with generic actions (e.g., “think about it / talk next week”) rather than a clear vision narrative.
- **3** (Sufficient): The candidate communicates a basic vision behind the change, typically linking it to broad organizational aims 
such as staying current, improving service, retaining customers, or responding to market developments. They provide a general “why” 
that goes beyond pure compliance and occasionally point to future benefits. They make a partial translation to Jolanda’s work, 
but the vision remains somewhat generic and not fully sharpened into a vivid future state. 
Future possibilities are mentioned, yet not consistently made concrete or inspiring.
*Example Behaviors*: Explains that the old approach is outdated and that the organization needs to “keep up with developments” 
to stay relevant and keep/attract customers. States that management chose this direction for a reason and suggests that 
the change should benefit customers in the long run. Connects policy to work activities in a basic way (e.g., Jolanda must understand 
the new agreements and communicate them clearly so customers can follow the transition). Mentions tools like training/toolbox 
or additional explanation to help staff deliver the new story. Frames the next step as clarifying what’s unclear so Jolanda 
can regain confidence and convey the new service convincingly.
- **4** (Good): The candidate communicates a clear, credible vision for why the organization is changing and what long‑term 
success looks like. They connect the change to organizational values and strategic goals, and translate policy into concrete meaning 
for Jolanda’s daily work. The message is future-focused and motivating, highlighting possibilities rather than only pressure. 
Vision is coherent, though not always highly vivid or inspirational.
*Example Behaviors*: Explains the “why” in specific terms (e.g., unity of policy protects trust/legitimacy, and consistent application ensures 
customers receive the same quality regardless of employee). Frames the change as part of “who we are” as an organization 
and how we want to be seen by customers. Links this to Jolanda’s role (e.g., she is a key carrier of the new story 
and must translate policy into clear customer communication). Emphasizes the future benefit (e.g., professional image, 
stable customer expectations) and invites reflection on barriers (e.g., “what blocks you?”). Summarizes the direction and next steps while keeping the vision central.
- **5** (Excellent): The candidate conveys a compelling, coherent vision that clearly links external developments 
to the organization’s long‑term direction and desired future state. They translate this vision into meaningful implications for Jolanda’s daily work. 
The message is future‑possibility focused, not just compliance. The candidate integrates Jolanda’s values/strengths into the vision, 
showing how she can remain authentic while becoming a key contributor to the change.
*Example Behaviors*: Frames the change as a response to shifting environment and client needs (e.g., “the organization and clients 
are changing, and we need to move with that”), then paints a future state (e.g., clear, consistent service; stronger trust; 
better fit with today’s demands). Connects Jolanda’s strengths (e.g., customer empathy, experience, sincerity) to the vision 
(e.g., “we need your way with clients to make this land”). Explains what the policy means in practice: one unified story, 
clear conditions, confident explanation of “why.” Invites contribution: identify where the new direction fits/doesn’t, 
formulate opportunities, and bring improvement questions back to the team/management.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Conveying a vision" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A detailed explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for the candidate's own priorities and values to understand the root of the dilemma.
  Synthesizes information from different scenes to form a coherent picture of the situation.

**Check for consistency**:
- Double-check that each score aligns with both the rubric criteria and the rationale provided.
- Maintain objectivity by strictly adhering to the rubric as written, without introducing personal interpretations or biases.

Transcript:
```{text}```
"""
    )
}