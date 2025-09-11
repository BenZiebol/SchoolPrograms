# 3081 Lab 11: Final Project Extension(s)
_(Due: Thursday, November 21st, 2024 @ 11:59pm)_

## Lab Instructions

### Goal
The primary goal of this lab is for your group to pick an extension(s) and start the final project. You will not be coding during this lab assignment. Instead, you will be writing EARS style requirements for your extension(s), a first draft of a UML class diagram for your extension(s), and writing Gherkin style test cases for your extension(s). Groups with two members should have one extension and groups with four members should have two extensions.


## Tasks

All group members are expected to work on this lab assignment together. Everyone will share each task. If you end up making decisions without your group (due to them being inactive, busy, etc.), please get them caught up on all decision making. If a group member refuses to contribute or get caught up by their teammates, do not add them to the Gradescope submission.

| ID | Title | Task Summary Description | Task Deliverable |
| :---: | --- | --- | --- |
| | Starting the Final Project | | |
| Task 1 | Choose extension(s) | Meet with your group and choose your extension(s) | Gradescope submission |
| Task 2 | Write EARS requirements | Write EARS style requirements for your extension(s) | Gradescope submission |
| Task 3 | Write UML class diagram | Create a first draft of your UML class diagram | Gradescope Submission |
| Task 4 | Write Gherkin test cases | Learn and write Gherkin style test cases for your extension(s) | Source code |

You must do these tasks in order. Remember that all these tasks are to be done collectively by everyone in your group.

### Task 1: Choose your extension(s)

Groups with two members must choose one extension. Groups with four members must choose two extensions.

We have provided a list of extensions that you may choose from. We have also included a link to the final project write up that has more detailed descriptions (albeit still somewhat vague for academic purposes) for each of these extensions. We recommend that you check out the link before you choose an extension, so that you’re more prepared with the extension(s) that you’re choosing.

The final project write up can be found on Canvas

| ID | Title | Extension Description | Design Pattern |
| :---: | --- | --- | --- |
| 1 | Battery Packs and Data Collection | Introduce batteries by decorating drones, recharge stations by extending the composite factory, and corresponding logic into the simulation. Use a singleton to collect interesting data (including battery use) during runtime and output the data. | Decorator and extending the Composite Factory and Singleton |
| 2 | Stop Signs and Action Replay | Introduce intersections and corresponding logic into the simulation. Introduce save states into the simulation (including stop sign state). | Mediator and extending the Composite Factory and Memento |
| 3 | Emergency Landing Protocol and Wallets and Refunds | Introduce route interruptions (ie fires, emergency vehicles, etc.) by extending the composite factory, emergency protocols by decorating drones, and corresponding logic into the simulation. Introduce money by decorating entities and corresponding logic (including refunding the customer in some emergency situations) into the simulation. | Decorator and extending the Composite Factory and Decorator |
| 4 | Frozen Food Delivery and Weather | Introduce cooled drones by decorating drones, cooling stations by extending the composite factory, and corresponding logic into the simulation. Use a singleton to rotate between different types of weather and temperature which affects the state of the drones and frozen delivery logic. | Decorator and extending the Composite Factory and Singleton and State |
| 5 | Custom Extension | Create an extension idea from scratch and get it checked off by the instructor | your choice |

**If you picked extension 5**: Once you have a concrete idea of what you want your extension to be (including the design pattern which will enable the extension to be of high quality), you **must** get it checked off with an instructor. Extensions which **do not** clearly incorporate a design pattern **will not** be approved. To have your custom extension approved, please email an instructor (Shonal) in order to set up time to discuss **before Monday, November 18th at 11:59 pm**. In addition, teams of 4 may only select option 5 for one of the non-trivial features they develop.

Reminder: Please go look at the final project write up to see some additional explanation for each task if needed.

Once your team has decided which extension(s) to implement, move onto the next task.

### Task 2: EARS requirements

You will be writing EARS (easy approach to requirements syntax) style requirements **only for your extension(s)**.

Recall the six types of requirements: ubiquitous, event-driven, unwanted behavior, state-driven, optional feature, and complex feature. Revisit lecture 6 or workshop 3 if needed.

Ubiquitous requirements: not invoked by an event detected at the system boundary or in response to a defined system state (always active).

```
The <system name> shall <system response>.
```

Event-driven requirements: initiated only when a triggering event is detected at the system boundary.

```
WHEN <optional preconditions> <trigger> the <system name> shall <system response>.
```

Unwanted behavior requirements: undesired situations such as failures, disturbances, or deviations from desired user behavior or unexpected behavior of interacting systems

```
IF <optional preconditions> <trigger>, THEN the <system name> shall <system response>.
```

State-driven requirements: active while the system is in a defined state.

```
WHILE <in a specific state> the <system name> shall <system response>.
```

Optional feature requirements: applicable only in systems that include a particular feature.

```
WHERE <feature is included> the <system name> shall <system response>.
```

Complex feature requirements: complex conditional clauses using combinations of WHEN, WHERE, and WHILE. One can mix and match these keywords to build complex expressions to specify richer system behaviors.

```
Example: While the aircraft is on-ground, when reverse thrust is commanded, the control system shall enable deployment of the thrust reverser.
Example: While the aircraft is in-flight, if reverse thrust is commanded, then the control system shall inhibit thrust reverser deployment.
Example: When selecting idle setting, if aircraft data is unavailable, then the control system shall select Approach Idle.
```

Write as many requirements (of all types) as you can for your extension(s). Your requirements may change as you continue working on the project and that’s okay.

Once you have a complete list of EARS style requirements ready to submit to Gradescope, move onto the next task.

### Task 3: UML Class Diagram

For this task, you must use [LucidChart](https://lucid.app/documents).

For your extension(s), create a first draft of your UML class diagram designs. Groups with two members are expected to have one UML class diagram and groups with four members are expected to have two UML class diagrams.

In your UML class diagram, only include parts of the existing simulation that interact with your extension(s). For example, if `WebServerBase` doesn’t interact with your extension(s) directly, do not include it in your draft. 

Additionally, we expect that each new class introduced into the simulation has a logical class name, member attributes, and member functions. Please use the UML style note/annotation shape to explain anything to us about your extension(s) that aren’t obvious.

You **must** use a design pattern to solve your extension(s) in your UML class diagram(s).

Remember that this is a first draft, so we expect it to be somewhat incomplete and also subject to change.

Once you have your UML class diagram(s) and are ready to submit them to Gradescope (as a file, not a link), move onto the next task.

### Task 4: Gherkin test cases
For this task, you will be writing test cases for your extension(s). These test cases will not be in the Google Test framework that you saw in homework 3. Instead, you will use Gherkin syntax to document behavior-driven development (BDD) test cases. Below, you’ll find a condensed version of a Gherkin Reference Manual attached as an appendix. Reading the appendix is required in order to complete this task.

Consider three realistic ways that your extension(s) will get used. For each of these ways, develop a Scenario, written in Gherkin syntax, that represents how you would determine if the action the user desires works or does not work.

Once you have **three** Gherkin style Scenarios **per extension** and they’re ready to submit to Gradescope, move onto the next task.

# Final Submission
**One submission per group. Designate someone to make the submission, then add members to the submission!**

Before submitting, make sure that...
- Your choices for extension(s) are from the list
   - if you picked a custom extension, it must be checked off by an instructor
- Your requirements for your extension(s) are as complete, clear, and concise
- Your UML class diagram clearly shows your extension(s) and how it is integrated into your current system by using a design pattern(s)
- Your Gherkin test scenarios cover common cases that pertain to your extension(s)

To submit your lab:

1. Submit your task deliverables to the Gradescope assignment "lab11: Final Project Extension(s)" with your team name. Only 1 group member should submit a Gradescope assignment for the lab. Make sure that you add your teammates to the submission. See the FAQ link below on how to do this. 

     [FAQ: Gradescope Group Submissions](https://github.umn.edu/umn-csci-3081w-f24-sec010/FAQ/tree/main/Gradescope%20Include%20Teammates)

Once you have submitted your deliverables to Gradescope and added your active team members to the submission, you have completed the lab.




# Appendix: Gherkin Reference Manual


For the "plain English test cases", we'll be using a formalized language structure called Gherkin syntax. Gherkin syntax is used to describe test cases in some testing frameworks, like Cucumber. You can learn more about Cucumber and how it works in the guides listed at the end of the write-up.
For our assignment, we'll be using a restricted set of Gherkin syntax, for simplicity. We will be using only the `Feature` , `Scenario`/`Example`, and `Steps` (`Given`, `When`, `Then`, `And`, or `But`). Each of these keywords is used to begin a line to provide the structure of our test cases.




## Feature
The purpose of the `Feature` keyword is to provide a high-level description of a software feature, and to group related scenarios.
The first primary keyword in a Gherkin document must always be `Feature`, followed by a `:` and a short text that describes the feature.
You can add free-form text underneath `Feature` to add `Descriptions`.
```
Feature: Guess the word




  The word guess game is a turn-based game for two players.
  The Maker makes a word for the Breaker to guess. The game
  is over when the Breaker guesses the Maker's word.




  Example: Maker starts a game
```
The name and the optional description have no special meaning. Their purpose is to provide a place for you to document important aspects of the `Feature`, such as a brief explanation and a list of business rules (general acceptance criteria).
The free format `Description` for `Feature` ends when you start a line with the keyword  `Example`  (or the alias keyword `Scenario` ).




### Descriptions
Free-form descriptions (as described above for `Feature`) can also be placed underneath `Example`/`Scenario`.
You can write anything you like, as long as no line starts with a keyword.




## Example
This is a *concrete example* that *illustrates* a business rule. It consists of a list of `Step`s.
The keyword `Scenario` is a synonym of the keyword `Example`.
You can have as many `Step`s as you like, but we recommend 3-5 steps per `Example`. Having too many `Step`s will cause the `Example`to lose its expressive power as a specification and documentation.
In addition to being a specification and documentation, an `Example`is also a test. As a whole, your `Example`s are an *executable specification* of the system.
`Example`s follow this same pattern:
	* Describe an initial context (`Given` steps)
	* Describe an event (`When` steps)
	* Describe an expected outcome (`Then` steps)




## Steps
Each step starts with `Given`, `When`, `Then`, `And`, or `But`.
Each step in a scenario executes one at a time, in the sequence you’ve written them in.
Keywords are not taken into account when looking for a step definition. This means you cannot have a `Given`, `When`, `Then`, `And` or `But` step with the same text as another step.
These steps are considered duplicates:
```Given there is money in my account
Then there is money in my account
```
This might seem like a limitation, but it forces you to come up with a less ambiguous, more clear domain language:
```Given my account has a balance of £430
Then my account should have a balance of £430
```




## Given
`Given` steps are used to describe the initial context of the system - the *scene* of the scenario. It is typically something that happened in the *past*.
The purpose of `Given` steps is to **put the system in a known state** before the user (or external system) starts interacting with the system (in the `When` steps). Avoid talking about user interaction in `Given`’s. If you were creating use cases, `Given`’s would be your preconditions.
It’s okay to have several `Given` steps (use `And` or `But` for number 2 and upwards to make it more readable).
Examples:
	* Mickey and Minnie have started a game
	* I am logged in
	* Joe has a balance of £42




## When
`When` steps are used to describe an event, or an *action*. This can be a person interacting with the system, or it can be an event triggered by another system.
Examples:
	* Guess a word
	* Invite a friend
	* Withdraw money








*Imagine it's 1922*
*Most software does something people could do manually (just not as efficiently).*
*Try hard to come up with examples that don’t make any assumptions about technology or user interface. Imagine it’s 1922, when there were no computers.*
*Implementation details should be hidden in the step definitions.*


## Then
`Then` steps are used to describe an *expected* outcome, or result.
An outcome *should* be on an **observable** output. That is, something that comes out of the system (report, user interface, message), and not a behaviour deeply buried inside the system (like a record in a database).
Examples:
	* See that the guessed word was wrong
	* Receive an invitation
	* Card should be swallowed




While it might be tempting to implement `Then` steps to look in the database - resist that temptation!
You should only verify an outcome that is observable for the user (or external system), and changes to a database are usually not.




## And, But
If you have successive `Given`’s or `Then`’s, you *could* write:
```Example: Multiple Givens
	Given one thing
	Given another thing
	Given yet another thing
	When I open my eyes
	Then I should see something
	Then I shouldn't see something else
```




Or, you could make the example more fluidly structured by replacing the successive `Given`’s or `Then`’s with `And`’s and `But`’s:
```Example: Multiple Givens
	Given one thing
	And another thing
	And yet another thing
	When I open my eyes
	Then I should see something
	But I shouldn't see something else
```




## *
Gherkin also supports using an asterisk (`*`) in place of any of the normal step keywords. This can be helpful when you have some steps that are effectively a *list of things*, so you can express it more like bullet points where otherwise the natural language of `And` etc might not read so elegantly.


For example:
```Scenario: All done
	Given I am out shopping
	And I have eggs
	And I have milk
	And I have butter
	When I check my list
	Then I don't need anything
```
Could be expressed as:
```Scenario: All done
	Given I am out shopping
	* I have eggs
	* I have milk
	* I have butter
	When I check my list
	Then I don't need anything
```




## Concrete Example
One concrete example would be that *Sunday isn’t Friday*.
```Feature: Is it Friday yet?
	Everybody wants to know when it's Friday




	Scenario: Sunday isn't Friday
    	Given today is Sunday
    	When I ask whether it's Friday yet
    	Then I should be told "Nope"
```
The first line of this file starts with the keyword `Feature`: followed by a name.
The second line is a brief `Description` of the `Feature`.
The fourth line, `Scenario: Sunday is not Friday` is a `Scenario`, which is a *concrete example* illustrating how the software should behave. We could have also used `Example` here instead of `Scenario`.
The last three lines starting with `Given`, `When` and `Then` are the steps of our `Scenario`, defining the conditions under which the test will be evaluated.




## Additional tips
Can be found in the Cucumber guide to [Writing better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/).
More information about Cucumber is included in their [10 minute Tutorial](https://cucumber.io/docs/guides/10-minute-tutorial/?lang=java#write-a-scenario). The Cucumber tool allows for Behavior-Driven Development (BDD), a close cousin of Test-Driven Development (TDD). Cucumber is generally a Java tool, but also works for JavaScript, Ruby, and Kotlin. Learn more about BDD in the [guide](https://cucumber.io/docs/bdd/).




