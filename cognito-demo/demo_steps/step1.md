---


---

<h1 id="enhancing-api-security-with-aws-cognito">Enhancing API Security with AWS Cognito</h1>
<p>In this tutorial we will walk through a practical exercise to create a secure API. We will begin by a creating <strong>Lambda function</strong> to handle backend logic and integrate it with <strong>API Gateway</strong>. Then, we will create an <strong>AWS Cognito User Pool</strong> to manage user sign-up and sign-in. Finally, we will secure our API using a <strong>Cognito Authorizer</strong>, ensuring that only authenticated users can access it.</p>
<h3 id="step-1----creating-the-lambda-function">Step 1 – Creating the Lambda Function</h3>
<ol>
<li>Navigate to <strong>Lambda</strong> in the AWS Management Console.</li>
<li>Click on <code>Create function</code>.</li>
<li>Provide a name for your function like ‘testing’ and change select Python as the runtime, then create the function.</li>
<li>In the lambda function editor, you can edit the code to whatever it is you wish, but in our case we will just change the body of the json to ‘Hello from Liwanag Backend!’. This function when ran will return statusCode 200, and the string which we changed.</li>
</ol>
<pre><code>import json
def  lambda_handler(event, context):
	# TODO implement
	return {
		'statusCode': 200,
		'body': json.dumps('Hello from Liwanag Backend!')
}
</code></pre>
<ol start="5">
<li>Then click the blue <code>Deploy</code> button to the left of the code to deploy the function.</li>
</ol>
<h3 id="step-2----setting-up-the-api-gateway">Step 2 – Setting up the API Gateway</h3>
<ol>
<li>Navigate to <strong>API Gateway</strong> in the AWS Management Console.</li>
<li>Click on <code>Create API</code>.</li>
<li>Scroll down to <strong>REST API</strong> then click <code>Build</code>.</li>
<li>Provide a name for the API like ‘cognito-integration-demo’, then create the API.</li>
<li>Then we will add a route by clicking <code>Create method</code>, selecting <code>GET</code> as the method type and Lambda function as the integration type. Select the lambda function you created earlier, then create the method.</li>
<li>Now click on the orange <code>Deploy API</code> button, and create a new stage with whatever name you wish to deploy the API.</li>
<li>In the stage details, copy the <code>Invoke URL</code> which we will use to redirect the user after they have been authorized.</li>
</ol>
<h3 id="step-3">Step 3</h3>
<ol>
<li>Navigate to <strong>Cognito</strong> in the AWS Management Console.</li>
<li>Click the three lines in the top left if the User pools tab isn’t visible, then click on <code>Create user pool</code>.</li>
<li>Provide a name such as ‘testdemo’, and select the email checkbox as a sign-in identifier. Don’t forget to paste the API Invoke URL in the <strong>Return URL section</strong>.</li>
<li>Open the sidebar of the user pool you just created and travel to <code>App clients</code>. Click on the <code>Login pages</code> tab and click on <code>Edit</code> in <strong>Managed login pages configuration</strong>.</li>
<li>Change the <strong>OAuth 2.0 grant types</strong> to <code>Implicit grant</code> ONLY!</li>
<li>Click on the orange <code>Save changes</code> button.</li>
</ol>
<h3 id="step-4----securing-api-gateway-with-cognito-authorizer">Step 4 – Securing API Gateway with Cognito Authorizer</h3>
<ol>
<li>Navigate to <strong>API Gateway</strong> in the AWS Management Console.</li>
<li>Click on the API Gateway you created earlier, then travel to the sidebar menu and click on <code>Authorizers</code>.</li>
<li>Click on <code>Create an authorizer</code> .</li>
<li>Provide a name for the authorizer like ‘Authorizerdemo’, then select <code>Cognito</code> as the authorizer type. Select the user pool you created earlier, and in the <strong>Token Source</strong> section, enter ‘Token’. Then create the authorizer.</li>
<li>Travel to the sidebar menu and click on <code>Resources</code>. Click on the green <code>GET</code> method execution and click <code>Edit</code> in <strong>Method request settings</strong> sections.</li>
<li>Select the ‘Authorizationdemo’ as the Authorization, and add ‘email’ in Authorization scopes.</li>
<li>Click on the orange <code>Save</code> button.</li>
</ol>
<h3 id="step-5----testing-the-setup">Step 5 – Testing the Setup</h3>
<ol>
<li>Navigate to <strong>Cognito</strong> in the AWS Management Console.</li>
<li>Click on the user pool you created earlier – the Overview section should open. Travel to the Reccommendations section and click the <code>View login page</code> hyperlink which will take you to the hosted UI to sign up/sign in a user.</li>
<li>In the hosted UI, click on <code>Create an account</code> and follow the steps to create an account.</li>
<li>Now travel to the <code>View login page</code> again and sign in with your user credentials.</li>
<li><strong>Cognito</strong> will now redirect you to the <strong>API Invoke URL</strong> after you have been authorized, and the <strong>API Gateway</strong> will run the <strong>Lambda function</strong> we had created!</li>
</ol>

