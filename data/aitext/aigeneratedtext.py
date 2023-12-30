# list of 1000 greetings in Python
greetings = [
"1	Playing for the Michigan State basketball team in the aftermath of a horrific shooting meant that the team had to take on the responsibility of representing the university in a difficult time. It required them to open themselves up to criticism and public scrutiny, but they felt it was important to show resilience and strength in the face of adversity. They wanted to show that, in spite of the tragedy, life goes on.",
"2	In 1985, a small plane carrying a load of cocaine crashed in the Chattahoochee National Forest in Georgia. The crash site was discovered by a US Forest Service worker, who found a bear munching on the drugs. The bear had gotten into the drug shipment - which was estimated to be worth over $15 million - and had eaten around 20 pounds of cocaine. The bear was dubbed ""Cocaine Bear,"" and the story quickly became a source of folk legend.

The incident gained even more traction when news outlets started to report on it, and in 2009, the story was adapted into a mockumentary called ÒCocaine Bear: The Legend of Elrod,Ó which was released on YouTube.

Now, the story of the Cocaine Bear is getting the big-screen treatment. The film, ""Cocaine Bear,"" follows the story of a young bear cub named Elrod who is raised by drug smugglers in the 1980s. After the plane carrying a shipment of cocaine crashes in the national forest, Elrod is forced to fend for himself and learns to survive in the wild. The film stars Andrew Lincoln, Jessica Chastain, and Woody Harrelson.

The film is a dark comedy and a",
"3	In 1985, a large black bear was discovered in the Chattahoochee National Forest in Georgia with a strange story. The bear had been spotted by hunters, and it was waddling around with a dead manÕs body in its mouth. After further investigation, it was discovered that the man had died from a drug overdose and that the bear had been scavenging the body for food. What was even more bizarre was that the bear had managed to open the manÕs backpack and consume the contents, which included over 75 pounds of cocaine that had been packed in plastic bags.

The bear was found to have a level of cocaine in its bloodstream that was seven times higher than the lethal dose for humans. It was eventually euthanized due to its extreme agitation and aggression. The animalÕs strange tale has since become a popular urban legend, and experts have warned against feeding wild animals, as it can pose a significant risk to both the animals and humans.",
"4	To make it, start by heating some oil in a large skillet over medium-high heat. Add in a pound of ground pork and cook until no longer pink, breaking it up with a wooden spoon as it cooks. Add in some minced garlic and dried herbs such as oregano, thyme, and rosemary, and season with salt and pepper. Cook for a few minutes until the herbs are fragrant.

Next, add 1 cup of long-grain white rice and stir to combine. Pour in 2 cups of chicken broth and bring to a boil. Reduce the heat to low, cover the skillet, and simmer for about 18 minutes, or until the rice is tender.

Meanwhile, heat 2 tablespoons of butter in a separate skillet over medium heat. Add in a large head of thinly sliced cabbage and sautŽ for about 10 minutes, stirring occasionally, until golden and caramelized.

Once the pork and rice is done, remove it from the heat and fluff the rice with a fork. To assemble the skillet, layer the cabbage over the bottom of the skillet, followed by the pork and rice mixture. Top with the remaining cabbage and press it down into the mixture with a spoon.

Cover the skillet and cook over.",

]

import pandas as pd
data = pd.DataFrame({"greeting": greetings})
data = data.sample(frac=1).reset_index(drop=True)
data.to_csv("greetings.txt", index=False)
