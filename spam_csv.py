import os

def create_spam_csv():
   spam_data = '''v1,v2
ham,"Hi how are you? Hope you're having a great day!"
spam,"CONGRATULATIONS! You've won a $1000 gift card! Click here to claim"
ham,"Meeting at 3pm tomorrow in the conference room"
spam,"FREE VIAGRA! Best prices guaranteed. Click now to order"
ham,"Can you pick up some milk on your way home?"
spam,"You've won an iPhone 15! You are the 1000th visitor. Claim now"
ham,"Thanks for the birthday wishes!"
spam,"Make $5000 working from home! Limited time offer"
ham,"The project deadline is next Friday"
spam,"Your account has been suspended. Click here to verify"
ham,"Let's grab lunch tomorrow"
spam,"Hot singles in your area! Click to chat now"
ham,"The report looks good, just need minor changes"
spam,"URGENT: Your payment is pending. Update details now"
ham,"Great presentation today, well done!"
spam,"Buy cheap watches! Rolex, Omega replicas available"
ham,"Can we reschedule our meeting to next week?"
spam,"Your Netflix subscription has expired. Renew now"
ham,"Don't forget to bring the documents tomorrow"
spam,"Get rich quick! Invest in crypto now! 1000% returns"
ham,"The kids loved the party yesterday"
spam,"Your car warranty is about to expire. Renew now"
ham,"Please review the attached document"
spam,"BREAKING: Make money fast with this secret method"
ham,"See you at the restaurant at 7pm"
spam,"Lose 20 pounds in 1 week! Magic pill available"
ham,"Could you send me the updated schedule?"
spam,"You've been selected for a special offer! Click now"
ham,"Great job on completing the project!"
spam,"Your PayPal account needs verification. Login now"
ham,"Remember to bring your laptop to the meeting"
spam,"Congratulations! You've won the lottery! Claim prize"
ham,"Happy anniversary! Have a wonderful day"
spam,"URGENT: Your bank account needs verification"
ham,"The weather is perfect for a picnic"
spam,"Make money online! Work from home opportunity"
ham,"Looking forward to seeing you this weekend"
spam,"Your credit card has been charged. Dispute now"
ham,"Did you get my email about the proposal?"
spam,"FREE iPhone giveaway! You're our lucky winner"
ham,"The team did a great job on the presentation"
spam,"ALERT: Suspicious activity on your account"
ham,"Can you share the meeting notes?"
spam,"Buy cheap medications online! No prescription needed"
ham,"The concert was amazing last night"
spam,"Your computer has a virus! Download cleaner now"
ham,"Please confirm your attendance for tomorrow"
spam,"Get 90% off designer brands! Limited time only"
ham,"The report is ready for your review"
spam,"Double your income with this amazing opportunity"
ham,"Thanks for helping with the project"
spam,"Your Amazon order needs confirmation. Click here"
ham,"Don't forget about the team lunch tomorrow"
spam,"WIN a free vacation! Click here to enter"
ham,"The client loved our proposal"
spam,"URGENT: Your account will be closed. Act now"'''

   os.makedirs('data', exist_ok=True)
    
  with open(os.path.join('data', 'spam.csv'), 'w', encoding='utf-8') as f:
        f.write(spam_data)
    
    print("spam.csv file has been created in the data directory")

if __name__ == "__main__":
    create_spam_csv()
