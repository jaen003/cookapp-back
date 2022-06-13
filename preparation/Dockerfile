FROM mcr.microsoft.com/dotnet/sdk:6.0
WORKDIR /src/app
COPY preparation.csproj ./
COPY entrypoint.sh ./
RUN chmod +x ./entrypoint.sh && \
    dotnet restore