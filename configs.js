const dotenv = require('dotenv');

module.exports = async ({options,resolveVariable, resolveConfigurationProperty}) => {
    // Load env vars into Serverless environment
    // You can do more complicated env var resolution with dotenv here

    // function resolveVariable which resolves provided variable string.
    // const stage = await resolveVariable('sls:stage');
    // const region = await resolveVariable('opt:region, self:provider.region, "us-east-1"');

    // function options  CLI params as passed to the command

    //function resolveConfigurationProperty which resolves specific service configuration property.
    // let env = 'local';
    // if (options.stage != null){
    //     env = options.stage
    // }
    const envVars = dotenv.config({path: '.env'}).parsed;
    return Object.assign(
        {},
        envVars,      // `dotenv` environment variables
        process.env   // system environment variables
    );
};
