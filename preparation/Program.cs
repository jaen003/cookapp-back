using preparation.src.diningTable.domain;
using preparation.src.diningTable.infrastructure;
using preparation.src.shared.infrastructure;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.addDomainEvents();
builder.Services.AddSingleton<RabbitmqEventBusConnector, RabbitmqEventBusConnector>();
builder.Services.AddTransient<RabbitmqQueueNameFormatter, RabbitmqQueueNameFormatter>();
builder.Services.AddTransient<RabbitmqExchangeNameFormatter, RabbitmqExchangeNameFormatter>();
builder.Services.AddTransient<JsonDomainEventDeserializer, JsonDomainEventDeserializer>();
builder.Services.AddTransient<RabbitmqEventBusConfigurer, RabbitmqEventBusConfigurer>();
builder.Services.AddTransient<RabbitmqDomainEventsConsumer, RabbitmqDomainEventsConsumer>();
builder.Services.AddTransient<MssqlDatabaseConfigurer, MssqlDatabaseConfigurer>();
builder.Services.AddTransient<DiningTableRepository, MssqlDiningTableRepository>();
var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseAuthorization();

app.MapControllers();

// Configure services

var eventBusConfigurer = app.Services.GetRequiredService<RabbitmqEventBusConfigurer>();
eventBusConfigurer.configure();

var databaseConfigurer = app.Services.GetRequiredService<MssqlDatabaseConfigurer>();
databaseConfigurer.configure();

var rabbitmqDomainEventConsumer = app.Services.GetRequiredService<RabbitmqDomainEventsConsumer>();
rabbitmqDomainEventConsumer.consume();

app.Run();
